import subprocess

from pathlib import Path


PROJECT_DIR = Path(__file__).parent

FILES_FOR_UPDATE = (
    PROJECT_DIR.joinpath(i)
    for i in (
        "tests/test_template_project_python.txt",
        "LICENSE",
        "Makefile",
        "mkdocks.yml",
        "pyproject.toml",
        "tox.ini",
    )
)

FOR_RENAME = (
    PROJECT_DIR.joinpath(i)
    for i in ("tests/test_template_project_python.txt", "template_project_python")
)


class GitUserInfo:
    """
    name = User Name
    email = user@email.com
    """

    def __init__(self):
        self.name = self.get_user_info("name")
        self.email = self.get_user_info("email")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(name={self.name!r},"
            f" email={self.email!r},"
        )

    @staticmethod
    def get_user_info(git_arg: str) -> str:
        result = subprocess.run(
            ["git", "config", f"user.{git_arg}"], stdout=subprocess.PIPE
        )
        return result.stdout.decode().strip()


class ProjectInfo:
    """
    project_name = project-title
    project_title = Project Title
    package_name = project_title
    """

    def __init__(self):
        self.project_name = PROJECT_DIR.name
        self.project_title = self.project_name.replace("-", " ").title()
        self.package_name = self.project_name.replace("-", "_")

    def __repr__(self):
        return (
            f"{self.__class__.__name__}"
            f"(project_name={self.project_name!r},"
            f" project_title={self.project_title!r},"
            f" package_name={self.package_name!r})"
        )


def read_file(file_path: Path) -> str:
    with open(file_path, mode="r") as f:
        content = f.read()
    return content


def write_file(file_path: Path, content: str) -> None:
    with open(file_path, mode="w") as f:
        f.write(content)


def rename(path: Path, project_info: ProjectInfo) -> None:
    print(path.name)
    if path.is_file():
        path.rename(Path(path.parent, f"test_{project_info.package_name}.py"))

    elif path.is_dir():
        path.rename(Path(path.parent, project_info.package_name))


def edit_file(
    filepath: Path, project_info: ProjectInfo, git_user_info: GitUserInfo
) -> None:
    print(filepath.name)
    replacements = (
        ("{project_name}", project_info.project_name),
        ("{project_title}", project_info.project_title),
        ("{package_name}", project_info.package_name),
        ("{git_user_name}", git_user_info.name),
        ("{git_user_email}", git_user_info.email),
    )
    file_content = read_file(filepath)
    for i in replacements:
        file_content = file_content.replace(*i)
    write_file(filepath, file_content)


def main():
    project_info = ProjectInfo()
    git_user_info = GitUserInfo()

    print("Editing files...")
    for file in FILES_FOR_UPDATE:
        edit_file(file, project_info, git_user_info)

    print("Renaming...")
    for i in FOR_RENAME:
        rename(i, project_info)


if __name__ == "__main__":
    main()
