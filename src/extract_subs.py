"""
python src/extract_subs.py --video_dir data/samples/video
→ 在 data/samples/subtitles/ 生成 *.srt
"""
import os, subprocess, argparse, pathlib, tqdm

def dump_sub(video_path, out_dir):
    vid = pathlib.Path(video_path).stem
    srt_out = f"{out_dir}/{vid}.srt"
    if os.path.exists(srt_out):         # 跳过已提取
        return
    # ① 先试 ffmpeg 内嵌字幕流
    cmd = ["ffmpeg", "-y", "-i", video_path, "-map", "0:s:0",
           srt_out, "-loglevel", "quiet"]
    if subprocess.call(cmd) != 0:
        # ② 若失败，生成空 srt，占位
        open(srt_out, "w").close()

def main(args):
    os.makedirs(args.out_dir, exist_ok=True)
    for mp4 in tqdm.tqdm(sorted(pathlib.Path(args.video_dir).glob("*.mp4"))):
        dump_sub(str(mp4), args.out_dir)

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--video_dir", required=True)
    p.add_argument("--out_dir", default="data/samples/subtitles")
    main(p.parse_args())