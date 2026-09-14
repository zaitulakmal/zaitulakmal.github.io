import numpy as np, subprocess, sys, json
W,H=896,1200
def load(p):
    raw=subprocess.run(['ffmpeg','-v','error','-i',p,'-f','rawvideo','-pix_fmt','rgba','-'],capture_output=True,check=True).stdout
    return np.frombuffer(raw,np.uint8).reshape(H,W,4).astype(np.float32)
def save(a,p,w):
    subprocess.run(['ffmpeg','-v','error','-y','-f','rawvideo','-pix_fmt','rgba','-s',f'{w}x{H}','-i','-',p],input=np.clip(a,0,255).astype(np.uint8).tobytes(),check=True)

bw=load(sys.argv[1]); col=load(sys.argv[2]); out=sys.argv[3]
E=int(sys.argv[4]) if len(sys.argv)>4 else 230
alpha=bw[:,:,3]>128
def edge(side):
    xs=[]
    for y in range(H):
        r=np.nonzero(alpha[y])[0]
        xs.append((r[0] if side=='l' else W-1-r[-1]) if len(r) else W)
    xs=np.array(xs,float)
    y0=int(np.argmax(xs<=2))              # first row touching the frame
    ys=np.arange(max(0,y0-90),y0-4)
    s=np.polyfit(ys,xs[ys],1)[0]           # px of inset lost per row (negative)
    return y0,abs(s)
params={}
for side in 'lr':
    y0,s=edge(side); params[side]=(y0,s)
print(json.dumps(params))

def build(img):
    o=np.zeros((H,W+2*E,4),np.float32)
    o[:,E:E+W]=img
    SEAM=6
    for side in 'lr':
        y0,sl=params[side]
        cols=img[:, SEAM:SEAM+30, :3] if side=='l' else img[:, W-SEAM-30:W-SEAM, :3]
        sub=img[:, 14:60] if side=='l' else img[:, W-60:W-14]
        wgt=(sub[:,:,3]>250).astype(np.float32)
        base=(sub[:,:,:3]*wgt[:,:,None]).sum(1)/np.maximum(wgt.sum(1),1)[:,None]   # opaque pixels only
        py0=min(params[side][0]+30,H-120)
        patch=(img[py0:H, SEAM:SEAM+36, :3] if side=='l' else img[py0:H, W-SEAM-36:W-SEAM, :3])
        from numpy.lib.stride_tricks import sliding_window_view as swv
        pb=np.pad(patch,((2,2),(2,2),(0,0)),mode='edge')
        blur=swv(pb,(5,5),axis=(0,1)).mean(axis=(-1,-2))
        tex=patch-blur                                    # fabric grain only
        ph,pw=tex.shape[:2]
        k=31; pad=np.pad(base,((k//2,k//2),(0,0)),mode='edge')
        ker=np.ones(k)/k
        base=np.stack([np.convolve(pad[:,c],ker,'valid') for c in range(3)],1)
        for y in range(max(0,y0-24),H):
            t=y-y0
            ext=E*(1-np.exp(-max(t,0)*max(sl,0.35)/E)) if t>0 else 0
            n=int(np.ceil(ext))+SEAM
            d=np.arange(-SEAM+1,n-SEAM+1)                 # d<=0 overwrites the seam columns inside the frame
            dist=np.clip(d,0,None)
            shade=1-0.10*(dist/np.maximum(ext,1))**2      # round off towards the outer edge
            ty=(y*7+dist*13)%ph; tx=(dist*5+y*3)%pw
            px=base[y][None,:]*shade[:,None]+tex[ty,tx]*0.9
            cov=np.where(d<=0,1.0,np.clip(ext-(d-1),0,1))
            if t<=0: 
                keep=d<=0
                d,px,cov=d[keep],px[keep],cov[keep]
            xs=(E-d) if side=='l' else (E+W-1+d)
            inside=(img[y, (-d if side=='l' else W-1+d)[d<=0], 3] if (d<=0).any() else None)
            # inside the frame only paint where the subject already is
            if (d<=0).any():
                m=d<=0
                src_a=img[y,(-d[m]) if side=='l' else (W-1+d[m]),3]
                cov[m]=np.maximum(src_a/255.0, 1.0 if t>0 else 0.0)
                # blend original with fill across the seam so there is no hard line
                w=((SEAM+d[m])/SEAM)[:,None]              # 0 at inner end, 1 at frame edge
                orig=img[y,(-d[m]) if side=='l' else (W-1+d[m]),:3]
                px[m]=orig*(1-w)+px[m]*w
            o[y,xs,:3]=px; o[y,xs,3]=255*cov
    return o
save(build(bw),out+'/bw-ext.png',W+2*E)
save(build(col),out+'/col-ext.png',W+2*E)
print('ok',W+2*E)
