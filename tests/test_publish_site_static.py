"""Static guards for the site publication sequence."""

from pathlib import Path
import unittest


ROOT = Path(__file__).resolve().parents[1]
PUBLISHER = ROOT / "scripts" / "publish_site.sh"


class PublishSiteStaticTests(unittest.TestCase):
    def test_publisher_validates_before_pushing_and_deploying(self):
        self.assertTrue(PUBLISHER.exists(), "publisher script is missing")
        script = PUBLISHER.read_text(encoding="utf-8")

        validate = "python3 scripts/validate_site.py"
        push = "git push origin main"
        deploy = "vercel --prod --yes"

        self.assertIn(validate, script)
        self.assertIn(push, script)
        self.assertIn(deploy, script)
        self.assertLess(script.index(validate), script.index(push))
        self.assertLess(script.index(push), script.index(deploy))

    def test_publisher_verifies_the_public_endpoint(self):
        self.assertTrue(PUBLISHER.exists(), "publisher script is missing")
        script = PUBLISHER.read_text(encoding="utf-8")

        probe = 'curl --fail --silent --show-error --max-time 20 "$SITE_URL" > /dev/null'

        self.assertIn('SITE_URL="${AMIRFISH_SITE_URL:-https://amirfish.ai}"', script)
        self.assertIn(probe, script)
        self.assertLess(script.index("vercel --prod --yes"), script.index(probe))


if __name__ == "__main__":
    unittest.main()
