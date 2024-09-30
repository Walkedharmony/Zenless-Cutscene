import argparse
import os
import subprocess
import sys
import Extract 

def main():
    parser = argparse.ArgumentParser(description="Zenless Cutscene - Extracting .usm files using WannaCRI Donmai-me")

    parser.add_argument("input", help="Input file name with .usm extension", type=str)

    parser.add_argument("-k", "--key", help="The key that will be used to extract the .usm file (17 digits)", required=True)

    args = parser.parse_args()

    if not args.input.endswith(".usm"):
        print(f"Error: File '{args.input}' not a file with the extension .usm", file=sys.stderr)
        sys.exit(1)

    if not os.path.isfile(args.input):
        print(f"Error: File '{args.input}' not found", file=sys.stderr)
        sys.exit(1)

    input_filename_without_ext = os.path.splitext(args.input)[0]

    try:
        print(f"Processing {args.input}...", end="", flush=True)

        command = ["wannacri", "extractusm", args.input, "--key", args.key]
        subprocess.run(command, check=True, capture_output=True, text=True)
        print(" DONE")

        output_audio_dir = os.path.join("output", input_filename_without_ext + ".usm", "videos")
        print(f"Processing Audio Extraction... to {output_audio_dir}")

        Extract.extract_audio_from_db(input_filename_without_ext, db_name="audio_files.db", output_folder=output_audio_dir) 
        print("Processing Audio... DONE")

        audio_file_path = os.path.join(output_audio_dir, f"{input_filename_without_ext}.aac")
        video_file_path = os.path.join(output_audio_dir, f"{input_filename_without_ext}.ivf")
        output_video_path = os.path.join(output_audio_dir, f"{input_filename_without_ext}.mp4")

        if not os.path.isfile(audio_file_path):
            print(f"Error: Audio file '{audio_file_path}' not found.", file=sys.stderr)
            sys.exit(1)

        print("Processing Merge...", end="", flush=True)
        ffmpeg_command = ["ffmpeg", "-i", video_file_path, "-i", audio_file_path, "-c:v", "copy", "-c:a", "aac", "-b:a", "320k", "-movflags", "+faststart", output_video_path]
    
        subprocess.run(ffmpeg_command, capture_output=True, text=True)
        print(" DONE")
        
        os.remove(video_file_path)
        os.remove(audio_file_path)

    except subprocess.CalledProcessError as e:
        print(f"Error: Gagal mengeksekusi perintah.\n{e.stderr}", file=sys.stderr)
        sys.exit(1)

if __name__ == "__main__":
    main()
