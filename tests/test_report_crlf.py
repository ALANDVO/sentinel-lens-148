import unittest

from cbh import cli


class ReportCrlfTests(unittest.TestCase):
    def test_crlf_frontmatter_and_sections_parse_like_lf(self):
        # A finding authored on Windows (CRLF) must parse identically to LF:
        # frontmatter keys and body sections are not lost to the \r.
        text = (
            "---\r\n"
            "severity: High\r\n"
            "asset: api.example.com\r\n"
            "---\r\n"
            "# Title\r\n"
            "\r\n"
            "## Summary\r\n"
            "summary body\r\n"
            "\r\n"
            "## Steps to reproduce\r\n"
            "1. curl x\r\n"
        )
        md = cli.parse_finding_metadata(text)
        self.assertEqual(md["severity"], "High")
        self.assertEqual(md["asset"], "api.example.com")
        self.assertEqual(md["summary"], "summary body")
        self.assertEqual(md["steps"], "1. curl x")


if __name__ == "__main__":
    unittest.main()
