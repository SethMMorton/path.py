from __future__ import annotations

import builtins
import contextlib
import os
import sys
from types import ModuleType, TracebackType
from typing import (
    IO,
    Any,
    AnyStr,
    Callable,
    Generator,
    Iterable,
    Iterator,
)

from _typeshed import (
    Self,
)

from . import classes

# Type for the match argument for several methods
_Match = str | Callable[[str], bool] | Callable[[Path], bool] | None

class TreeWalkWarning(Warning):
    pass

class Traversal:
    follow: Callable[[Path], bool]

    def __init__(self, follow: Callable[[Path], bool]): ...
    def __call__(
        self,
        walker: Generator[Path, Callable[[], bool] | None, None],
    ) -> Iterator[Path]: ...

class Path(str):
    module: Any

    def __init__(self, other: Any = ...) -> None: ...
    @classmethod
    def using_module(cls, module: ModuleType) -> type[Path]: ...
    @classes.ClassProperty
    @classmethod
    def _next_class(cls: type[Self]) -> type[Self]: ...
    def __repr__(self) -> str: ...
    def __add__(self: Self, more: str) -> Self: ...
    def __radd__(self: Self, other: str) -> Self: ...
    def __div__(self: Self, rel: str) -> Self: ...
    def __truediv__(self: Self, rel: str) -> Self: ...
    def __rdiv__(self: Self, rel: str) -> Self: ...
    def __rtruediv__(self: Self, rel: str) -> Self: ...
    def __enter__(self: Self) -> Self: ...
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...
    @classmethod
    def getcwd(cls: type[Self]) -> Self: ...
    def absolute(self: Self) -> Self: ...
    def abspath(self: Self) -> Self: ...
    def normcase(self: Self) -> Self: ...
    def normpath(self: Self) -> Self: ...
    def realpath(self: Self) -> Self: ...
    def expanduser(self: Self) -> Self: ...
    def expandvars(self: Self) -> Self: ...
    def dirname(self: Self) -> Self: ...
    def basename(self: Self) -> Self: ...
    def expand(self: Self) -> Self: ...
    @property
    def stem(self) -> str: ...
    def with_stem(self: Self, stem: str) -> Self: ...
    @property
    def suffix(self: Self) -> Self: ...
    @property
    def ext(self) -> str: ...
    def with_suffix(self: Self, suffix: str) -> Self: ...
    @property
    def drive(self: Self) -> Self: ...
    @property
    def parent(self: Self) -> Self: ...
    @property
    def name(self: Self) -> Self: ...
    def with_name(self: Self, name: str) -> Self: ...
    def splitpath(self: Self) -> tuple[Self, str]: ...
    def splitdrive(self: Self) -> tuple[Self, Self]: ...
    def splitext(self: Self) -> tuple[Self, str]: ...
    def stripext(self: Self) -> Self: ...
    @classes.multimethod
    def joinpath(cls: Self, first: str, *others: str) -> Self: ...
    def splitall(self: Self) -> list[Self | str]: ...
    def parts(self: Self) -> tuple[Self | str, ...]: ...
    def _parts(self: Self) -> Iterator[Self | str]: ...
    def _parts_iter(self: Self) -> Iterator[Self | str]: ...
    def relpath(self: Self, start: str = ...) -> Self: ...
    def relpathto(self: Self, dest: str) -> Self: ...

    # --- Listing, searching, walking, and matching
    def iterdir(self: Self, match: _Match = ...) -> Iterator[Self]: ...
    def listdir(self: Self, match: _Match = ...) -> list[Self]: ...
    def dirs(self: Self, match: _Match = ...) -> list[Self]: ...
    def files(self: Self, match: _Match = ...) -> list[Self]: ...
    def walk(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Generator[Self, Callable[[], bool] | None, None]: ...
    def walkdirs(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Iterator[Self]: ...
    def walkfiles(
        self: Self,
        match: _Match = ...,
        errors: str = ...,
    ) -> Iterator[Self]: ...
    def fnmatch(
        self,
        pattern: Path | str,
        normcase: Callable[[str], str] | None = ...,
    ) -> bool: ...
    def glob(self: Self, pattern: str) -> list[Self]: ...
    def iglob(self: Self, pattern: str) -> Iterator[Self]: ...
    def bytes(self) -> builtins.bytes: ...
    def write_bytes(self, bytes: builtins.bytes, append: bool = ...) -> None: ...
    def read_text(
        self, encoding: str | None = ..., errors: str | None = ...
    ) -> str: ...
    def read_bytes(self) -> builtins.bytes: ...
    def text(self, encoding: str | None = ..., errors: str = ...) -> str: ...
    def lines(
        self,
        encoding: str | None = ...,
        errors: str | None = ...,
        retain: bool = ...,
    ) -> list[str]: ...
    def write_lines(
        self,
        lines: list[str],
        encoding: str | None = ...,
        errors: str = ...,
        linesep: str | None = ...,
        append: bool = ...,
    ) -> None: ...
    def read_md5(self) -> builtins.bytes: ...
    def read_hash(self, hash_name: str) -> builtins.bytes: ...
    def read_hexhash(self, hash_name: str) -> str: ...
    def isabs(self) -> bool: ...
    def exists(self) -> bool: ...
    def isdir(self) -> bool: ...
    def is_dir(self) -> bool: ...
    def isfile(self) -> bool: ...
    def is_file(self) -> bool: ...
    def islink(self) -> bool: ...
    def ismount(self) -> bool: ...
    def samefile(self, other: str) -> bool: ...
    def getatime(self) -> float: ...
    @property
    def atime(self) -> float: ...
    def getmtime(self) -> float: ...
    @property
    def mtime(self) -> float: ...
    def getctime(self) -> float: ...
    @property
    def ctime(self) -> float: ...
    def getsize(self) -> int: ...
    @property
    def size(self) -> int: ...
    def access(
        self,
        mode: int,
        *,
        dir_fd: int | None = ...,
        effective_ids: bool = ...,
        follow_symlinks: bool = ...,
    ) -> bool: ...
    def stat(self) -> os.stat_result: ...
    def lstat(self) -> os.stat_result: ...
    def get_owner(self) -> str: ...
    @property
    def owner(self) -> str: ...

    if sys.platform != 'win32':
        def statvfs(self) -> os.statvfs_result: ...
        def pathconf(self, name: str | int) -> int: ...

    def utime(
        self,
        times: tuple[int, int] | tuple[float, float] | None = ...,
        *,
        ns: tuple[int, int] = ...,
        dir_fd: int | None = ...,
        follow_symlinks: bool = ...,
    ) -> Path: ...
    def chmod(self: Self, mode: str | int) -> Self: ...

    if sys.platform != 'win32':
        def chown(self: Self, uid: int | str = ..., gid: int | str = ...) -> Self: ...

    def rename(self: Self, new: str) -> Self: ...
    def renames(self: Self, new: str) -> Self: ...
    def mkdir(self: Self, mode: int = ...) -> Self: ...
    def mkdir_p(self: Self, mode: int = ...) -> Self: ...
    def makedirs(self: Self, mode: int = ...) -> Self: ...
    def makedirs_p(self: Self, mode: int = ...) -> Self: ...
    def rmdir(self: Self) -> Self: ...
    def rmdir_p(self: Self) -> Self: ...
    def removedirs(self: Self) -> Self: ...
    def removedirs_p(self: Self) -> Self: ...
    def touch(self: Self) -> Self: ...
    def remove(self: Self) -> Self: ...
    def remove_p(self: Self) -> Self: ...
    def unlink(self: Self) -> Self: ...
    def unlink_p(self: Self) -> Self: ...
    def link(self: Self, newpath: str) -> Self: ...
    def symlink(self: Self, newlink: str | None = ...) -> Self: ...
    def readlink(self: Self) -> Self: ...
    def readlinkabs(self: Self) -> Self: ...
    def copyfile(self, dst: str, *, follow_symlinks: bool = ...) -> str: ...
    def copymode(self, dst: str, *, follow_symlinks: bool = ...) -> None: ...
    def copystat(self, dst: str, *, follow_symlinks: bool = ...) -> None: ...
    def copy(self, dst: str, *, follow_symlinks: bool = ...) -> Any: ...
    def copy2(self, dst: str, *, follow_symlinks: bool = ...) -> Any: ...
    def copytree(
        self,
        dst: str,
        symlinks: bool = ...,
        ignore: Callable[[str, list[str]], Iterable[str]] | None = ...,
        copy_function: Callable[[str, str], None] = ...,
        ignore_dangling_symlinks: bool = ...,
        dirs_exist_ok: bool = ...,
    ) -> Any: ...
    def move(
        self, dst: str, copy_function: Callable[[str, str], None] = ...
    ) -> Any: ...
    def rmtree(
        self,
        ignore_errors: bool = ...,
        onerror: Callable[[Any, Any, Any], Any] | None = ...,
    ) -> None: ...
    def rmtree_p(self: Self) -> Self: ...
    def chdir(self) -> None: ...
    def cd(self) -> None: ...
    def merge_tree(
        self,
        dst: str,
        symlinks: bool = ...,
        *,
        copy_function: Callable[[str, str], None] = ...,
        ignore: Callable[[Any, list[str]], list[str] | set[str]] = ...,
    ) -> None: ...

    if sys.platform != 'win32':
        def chroot(self) -> None: ...

    if sys.platform == 'win32':
        def startfile(self: Self, operation: str | None = ...) -> Self: ...

    @contextlib.contextmanager
    def in_place(
        self,
        mode: str = ...,
        buffering: int = ...,
        encoding: str | None = ...,
        errors: str | None = ...,
        newline: str | None = ...,
        backup_extension: str | None = ...,
    ) -> Iterator[tuple[IO[Any], IO[Any]]]: ...
    @classes.ClassProperty
    @classmethod
    def special(cls) -> Callable[[str | None], SpecialResolver]: ...

class DirectoryNotEmpty(OSError):
    @staticmethod
    def translate() -> Iterator[None]: ...

def only_newer(copy_func: Callable[[str, str], None]) -> Callable[[str, str], None]: ...

class ExtantPath(Path):
    def _validate(self) -> None: ...

class ExtantFile(Path):
    def _validate(self) -> None: ...

class SpecialResolver:
    class ResolverScope:
        def __init__(self, paths: SpecialResolver, scope: str) -> None: ...
        def __getattr__(self, class_: str) -> MultiPathType: ...

    def __init__(
        self,
        path_class: type,
        appname: str | None = ...,
        appauthor: str | None = ...,
        version: str | None = ...,
        roaming: bool = ...,
        multipath: bool = ...,
    ): ...
    def __getattr__(self, scope: str) -> ResolverScope: ...
    def get_dir(self, scope: str, class_: str) -> MultiPathType: ...

class Multi:
    @classmethod
    def for_class(cls, path_cls: type) -> type[MultiPathType]: ...
    @classmethod
    def detect(cls, input: str) -> MultiPathType: ...
    def __iter__(self) -> Iterator[Path]: ...
    @classes.ClassProperty
    @classmethod
    def _next_class(cls) -> type[Path]: ...

class MultiPathType(Multi, Path):
    pass

class TempDir(Path):
    @classes.ClassProperty
    @classmethod
    def _next_class(cls) -> type[Path]: ...
    def __new__(
        cls: type[Self],
        suffix: AnyStr | None = ...,
        prefix: AnyStr | None = ...,
        dir: AnyStr | os.PathLike[AnyStr] | None = ...,
    ) -> Self: ...
    def __init__(self) -> None: ...
    def __enter__(self) -> Path: ...  # type: ignore
    def __exit__(
        self,
        exc_type: type[BaseException] | None,
        exc_val: BaseException | None,
        exc_tb: TracebackType | None,
    ) -> None: ...

class Handlers:
    @classmethod
    def _resolve(cls, param: str | Callable[[str], None]) -> Callable[[str], None]: ...
