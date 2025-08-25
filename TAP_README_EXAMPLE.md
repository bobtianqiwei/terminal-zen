# Bob Tianqi Wei's Homebrew Tap

This repository contains Homebrew formulas for my various projects and tools.

## Installation

Add this tap to your Homebrew installation:

```bash
brew tap bobtianqiwei/tap
```

## Available Formulas

### terminal-zen
A terminal-based breathing and meditation guide with ASCII progress bars.

```bash
brew install terminal-zen
```

**Features:**
- Zero dependencies (Python standard library only)
- Interactive breathing sessions (1, 3, or 10 minutes)
- Configurable breathing patterns
- Visual progress bars
- Philosophical quotes upon completion

### another-project (Example)
Description of another project.

```bash
brew install another-project
```

### my-cli-tool (Example)
Description of a CLI tool.

```bash
brew install my-cli-tool
```

## Development

To add a new formula to this tap:

1. Create a `.rb` file named after your project
2. Follow the Homebrew formula conventions
3. Test locally: `brew install --build-from-source ./formula-name.rb`
4. Commit and push to this repository

## Formula Examples

### Python Package Formula
```ruby
class ProjectName < Formula
  desc "Description of your project"
  homepage "https://github.com/bobtianqiwei/project-name"
  url "https://github.com/bobtianqiwei/project-name/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "SHA256_HASH"
  license "MIT"
  
  depends_on "python@3.9"
  
  def install
    system "python3", "-m", "pip", "install", *std_pip_args, "."
  end
  
  test do
    system "#{bin}/command-name", "--help"
  end
end
```

### Go Binary Formula
```ruby
class GoProject < Formula
  desc "Description of your Go project"
  homepage "https://github.com/bobtianqiwei/go-project"
  url "https://github.com/bobtianqiwei/go-project/archive/refs/tags/v1.0.0.tar.gz"
  sha256 "SHA256_HASH"
  license "MIT"
  
  depends_on "go" => :build
  
  def install
    system "go", "build", *std_go_args, "./cmd/project"
  end
  
  test do
    system "#{bin}/project", "--version"
  end
end
```

## License

This tap is licensed under the MIT License.
