"""
FAISS 余弦索引 (InnerProduct + L2-norm)
"""

import numpy as np
import faiss, json, argparse

p = argparse.ArgumentParser()
p.add_argument("--feats", default="feats.npy")
p.add_argument("--names", default="feats.json")
p.add_argument("--out",   default="clip.index")
args = p.parse_args()

xb = np.load(args.feats).astype("float32")
faiss.normalize_L2(xb)
index = faiss.IndexFlatIP(xb.shape[1])
index.add(xb)
faiss.write_index(index,args.out)
print("Indexed",index.ntotal, "videos")