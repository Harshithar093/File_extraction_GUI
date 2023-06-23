import zipfile


def archive_extract(archivepath, dest_dir):
    with zipfile.ZipFile(archivepath, 'r') as archive:
        archive.extractall(dest_dir)


if __name__ == "__main__":
    archive_extract("/Users/harshitha.r1/PycharmProjects/Preconfig/bonus/dest/compressed.zip",
                    "/Users/harshitha.r1/PycharmProjects/Preconfig/bonus/files")
