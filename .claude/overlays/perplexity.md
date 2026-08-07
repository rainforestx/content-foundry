# perplexity - content-foundry overlay

Applied over the `perplexity` skill's defaults when it runs in the article
pipeline. Only what is true of THIS repository.

## Every claim has to reach the claims table

The pipeline's standing rule is that a claim which cannot go on the claims
table does not ship, and absences are stated to the reader rather than padded.
That makes the useful output of a lookup a **fetchable primary source**, not an
answer. `perplexity_search` to locate and a fetch to read is the shape; a
synthesised answer with citations has not moved a claim onto the table, because
the table wants the document.

Magic-byte-verify every PDF (`%PDF` in the first eight bytes) and record the
edition and date. A saved 404 page with a `.pdf` extension is the failure that
rule exists for.

## Provenance can be the only evidence

Generations of the same product are often externally near-identical, so an
image or a datasheet that looks right proves nothing. The asset number, the
portal folder, or the document control number is the evidence; visual
similarity is not. Where a document's generation cannot be established from
its own imprint, it is not a source for a generation-specific claim, however
convincing the page looks.

`search_recency_filter` matters more here than almost anywhere: a
three-year-old page about a product line that has since had a generation
change is confidently, specifically wrong, and it will read as authoritative.

## Region

Set `country: "GB"`. The audience is UK, and availability, pricing, NHS versus
private routing and product naming all diverge by market. A US page answering a
UK question is a lead, not a source. Say which market a document describes when
it is not the UK.

## Check the acquisitions queue before searching

`pilot/ACQUISITIONS.md` is the standing list of documents the pipeline needs
and cannot reach, with URLs already pinned and each item saying what it
unblocks. Read it before running a sweep: the document you are about to hunt
for may already be pinned, already fetched into the Drive archive, or already
known to be the wrong generation. Add what you pin; remove what you verify.

## earx-catalogue is read-only from here

It is the substrate this pipeline harvests, not a place to write. Any agent
touching it reports `git status --porcelain` verbatim and it must be empty.
That guarantee is a promise made to other agents, not a preference, so it holds
even under an operator instruction that did not name it.
