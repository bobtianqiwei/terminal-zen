{
  inputs.nixpkgs.url = "github:NixOS/nixpkgs/nixpkgs-unstable";

  outputs = { self, nixpkgs, ... }:
    let
      supportedSystems = [ "x86_64-linux" "x86_64-darwin" "aarch64-linux" "aarch64-darwin" ];
      forAllSystems = nixpkgs.lib.genAttrs supportedSystems;
      pkgs = forAllSystems (system: nixpkgs.legacyPackages.${system});
      pkgMeta = with nixpkgs.lib; {
        description = "A terminal-based breathing and meditation guide with progress bars";
        homepage = "https://github.com/bobtianqiwei/terminal_zen";
        license = licenses.mit;
        maintainers = [ ];
        mainProgram = "zen";
      };
    in
    {
      packages = forAllSystems
        (system: {
          default = pkgs.${system}.python313Packages.buildPythonApplication
            {
              pname = "terminal_zen";
              version = "1.0.0";

              src = ./.;

              pyproject = true;

              build-system = with pkgs.${system}.python313Packages; [
                setuptools
                wheel
              ];

              pythonImportsCheck = [ "terminal_zen" ];

              meta = pkgMeta;
            };
        });

      devShells = forAllSystems (system: {
        default = pkgs.${system}.mkShellNoCC {
          packages = with pkgs.${system}; [
            python313
            python313Packages.setuptools
            python313Packages.wheel
            python313Packages.build
          ];
        };
      });

      apps = forAllSystems (system: {
        default = {
          type = "app";
          program = "${self.packages.${system}.default}/bin/zen";
          meta = pkgMeta;
        };
      });
    };
}
