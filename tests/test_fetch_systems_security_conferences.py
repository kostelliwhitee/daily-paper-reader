import importlib.util
import pathlib
import sys
import unittest


def _load_module(module_name: str, path: pathlib.Path):
    spec = importlib.util.spec_from_file_location(module_name, path)
    mod = importlib.util.module_from_spec(spec)
    assert spec and spec.loader
    sys.modules[module_name] = mod
    spec.loader.exec_module(mod)
    return mod


class FetchSystemsSecurityConferencesTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        root = pathlib.Path(__file__).resolve().parents[1]
        src_dir = root / "src"
        if str(src_dir) not in sys.path:
            sys.path.insert(0, str(src_dir))
        cls.mod = _load_module(
            "fetch_systems_security_conferences_mod",
            src_dir / "maintain" / "fetchers" / "fetch_systems_security_conferences.py",
        )

    def test_parse_osdi_paper_page_uses_citation_pdf_url(self):
        html = """
        <meta name="citation_title" content="A Real OSDI Paper">
        <meta name="citation_author" content="Ada Lovelace">
        <meta name="citation_author" content="Grace Hopper">
        <meta name="citation_publication_date" content="2025/07/07">
        <meta name="citation_pdf_url" content="https://www.usenix.org/system/files/osdi25-demo.pdf">
        <div class="field-name-field-paper-description"><p>Abstract text.</p></div>
        """
        paper = self.mod.parse_osdi_paper_page(html, year=2025, page_url="https://www.usenix.org/conference/osdi25/presentation/demo")
        self.assertEqual(paper["source"], "OSDI-2025-USENIX")
        self.assertEqual(paper["title"], "A Real OSDI Paper")
        self.assertEqual(paper["authors"], ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(paper["published"], "2025-07-07T00:00:00Z")
        self.assertEqual(paper["pdf_url"], "https://www.usenix.org/system/files/osdi25-demo.pdf")

    def test_parse_ndss_paper_page_finds_official_paper_pdf(self):
        html = """
        <h1>NDSS Paper Title</h1>
        <a class="pdf-button" href="https://www.ndss-symposium.org/wp-content/uploads/2026-f797-paper.pdf">Paper</a>
        <strong>Authors:</strong> Alice, Bob
        <h3>Abstract:</h3><p>NDSS abstract.</p>
        """
        paper = self.mod.parse_ndss_paper_page(html, year=2026, page_url="https://www.ndss-symposium.org/ndss-paper/demo/")
        self.assertEqual(paper["source"], "NDSS-2026-Accepted")
        self.assertEqual(paper["title"], "NDSS Paper Title")
        self.assertEqual(paper["pdf_url"], "https://www.ndss-symposium.org/wp-content/uploads/2026-f797-paper.pdf")

    def test_parse_sosp_accepted_page_pairs_titles_and_authors(self):
        html = """
        <ul class="paperlist">
          <li><b>Rearchitecting the Thread Model</b><br><em>Ada Lovelace, Grace Hopper</em></li>
          <li><b>Device-Assisted Live Migration</b><br><em>Barbara Liskov</em></li>
        </ul>
        """
        papers = self.mod.parse_sosp_accepted_page(html, year=2025)
        self.assertEqual([p["title"] for p in papers], ["Rearchitecting the Thread Model", "Device-Assisted Live Migration"])
        self.assertEqual(papers[0]["authors"], ["Ada Lovelace", "Grace Hopper"])
        self.assertEqual(papers[0]["source"], "SOSP-2025-ACM")

    def test_build_acm_pdf_url_from_doi(self):
        self.assertEqual(
            self.mod.build_acm_pdf_url("10.1145/3731569.3764794"),
            "https://dl.acm.org/doi/pdf/10.1145/3731569.3764794",
        )

    def test_ieee_sp_keeps_only_public_pdf_articles(self):
        articles = [
            {"id": "open", "title": "Open Paper", "authors": [{"fullName": "Ada"}], "isOpenAccess": True, "hasPdf": True, "fno": "313000a001", "doi": "10.1109/SP.1", "year": "2024"},
            {"id": "locked", "title": "Locked Paper", "authors": [{"fullName": "Bob"}], "isOpenAccess": False, "hasPdf": True, "fno": "223600a001", "doi": "10.1109/SP.2", "year": "2025"},
            {"id": "front", "title": "Title Page", "authors": [], "isOpenAccess": True, "hasPdf": True, "fno": "223600z001", "doi": "10.1109/SP.3", "year": "2025"},
        ]
        papers = self.mod.normalize_ieee_sp_articles(articles, year=2025, require_public_pdf=True)
        self.assertEqual(len(papers), 1)
        self.assertEqual(papers[0]["id"], "ieee-sp-2025-open-paper")
        self.assertEqual(
            papers[0]["pdf_url"],
            "https://www.computer.org/csdl/pds/api/csdl/proceedings/download-article/open/pdf",
        )


if __name__ == "__main__":
    unittest.main()
