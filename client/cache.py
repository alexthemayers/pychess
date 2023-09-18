class Cache:
    # TODO wtf is a cache list?!
    cache_list: list = []
    cache_filename: str = "board_cache0000.json"

    # TODO do we really need all these class methods?
    @classmethod
    def get_cache(cls) -> bool:
        if cls.cache_list is None:
            cls.write_cache(cls.cache_filename)
            return True
        else:
            filename = str(len(cls.cache_list)).join(cls.cache_filename.split("0000"))
            cls.write_cache(filename)
            return True

    @classmethod
    def clean(cls, path: str) -> bool:
        cache_limit: Optional[int] = None
        del_me: List[str] = []
        if path in cls.cache_list.values():
            for k, v in cls.cache_list.items():
                while v != path:
                    continue
                cache_limit = k
                break

            assert (type(
                cache_limit) is int), f"clean cache function failure. cache_limit should contain an integer, not {type(cache_limit)}"
            cls.cache_list = {key: value if key <= cache_limit else del_me.append(value) for key, value in
                              cls.cache_list.items()}
            # should recreate cache_list retaining only values that were generated up to the most recent cache point
            for file in del_me:
                os.unlink(file)
            return True
        else:
            print("could not find filename in cache list")
            return False

    @classmethod
    def __write_to_cache(cls, path: str) -> bool:
        with open(path, "a") as f:
            if f.write(dumps(cls.board)) > 0:
                cls.cache_list[len(cls.cache_list)] = str(cls.cache_filename)
                f.close()
                return True
            else:
                return False

    @classmethod
    def __read_from_cache(cls, path: str) -> Board:
        with open(path, "r") as f:
            if f is not None:
                b: Board = loads(f.read())
                f.close()
                cls.clean_cache(path)
                return b
            # TODO How do we throw an exception here?


if __name__ == "__main__":
    print("run main.py")
    exit(1)
