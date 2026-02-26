from portfolio_api.adapters.http.server import run
from portfolio_api.composition_root.bootstrap import build_list_projects_use_case


def main() -> None:
    use_case = build_list_projects_use_case()
    run(use_case)


if __name__ == "__main__":
    main()
