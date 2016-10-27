## imports
from oncotreenx import build_oncotree, get_basal, lookup_text

## testing classes
class TestOncotreenxConstruction:

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup(self):
        pass

    def teardown(self):
        pass

    def test_build_oncotree(self):

        # build the tree.
        g = build_oncotree()

        # assert we have some nodes.
        assert len(g.nodes()) > 10

class TestOncotreenxMethods:

    g = None

    @classmethod
    def setup_class(cls):
        pass

    @classmethod
    def teardown_class(cls):
        pass

    def setup(self):
        self.g = build_oncotree(file_path="data/oncotree_file.txt")

    def teardown(self):
        pass

    def test_get_basal(self):

        # get the ancestor.
        p = get_basal(self.g, "CCHDM")

        # make sure it is correct.
        assert 'BONE' == p
        assert False

    def test_text_lu(self):

        # get the ancestor.
        p = lookup_text(self.g, "Adrenal Gland")

        # make sure it is correct.
        assert 'ADRENAL_GLAND' == p