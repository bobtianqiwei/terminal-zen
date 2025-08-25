# terminal-zen.rb developed by Bob Tianqi Wei
class TerminalZen < Formula
  desc "A terminal-based breathing and meditation guide with progress bars"
  homepage "https://github.com/bobtianqiwei/terminal-zen"
  url "https://github.com/bobtianqiwei/terminal-zen/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "831e9ad87dc21cf3ac4e3e6a1b8cf184eb9887865034fdcc270a5125de26c835"
  license "MIT"
  head "https://github.com/bobtianqiwei/terminal-zen.git", branch: "main"

  depends_on "python@3.9"

  def install
    system "python3", "-m", "pip", "install", *std_pip_args, "."
  end

  test do
    system "#{bin}/zen", "--help"
  end
end
