import tempfile
import unittest
from pathlib import Path

from zenkb.chunker import chunk_markdown_files, validate_chunks


class ChunkerTest(unittest.TestCase):
    def test_frontmatter_and_heading_chunks(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            source = root / "Source"
            source.mkdir()
            doc = source / "sample.md"
            doc.write_text(
                "\n".join(
                    [
                        "---",
                        "title: Sample Doc",
                        "platforms: [amazon, flipkart]",
                        "---",
                        "",
                        "# Sample",
                        "",
                        "Intro text.",
                        "",
                        "## Details",
                        "",
                        "More text.",
                    ]
                ),
                encoding="utf-8",
            )

            chunks = chunk_markdown_files(source)
            validation = validate_chunks(chunks)

            self.assertTrue(validation.ok)
            self.assertEqual(validation.source_doc_count, 1)
            self.assertEqual(len(chunks), 2)
            self.assertEqual(chunks[0].frontmatter["title"], "Sample Doc")
            self.assertEqual(chunks[0].frontmatter["platforms"], ["amazon", "flipkart"])
            self.assertEqual(chunks[1].heading_path, ["Sample", "Details"])


if __name__ == "__main__":
    unittest.main()
