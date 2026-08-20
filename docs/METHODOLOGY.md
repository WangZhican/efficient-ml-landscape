# Methodology

## Goal

Build a high-recall, high-precision, auditable research map for Efficient ML / AI Infrastructure rather than a flat paper dump.

## Inclusion

Retain work with meaningful technical contribution, influence, systems value, architecture value, deployment relevance, or roadmap importance. There is no fixed paper-count cap.

Preference is given, all else being similar, to work with official open-source code/models/runtimes and stronger community adoption.

## Evidence hierarchy

Paper links should prefer:

1. arXiv or official proceedings paper page/PDF
2. official project or author page
3. publisher DOI page

Repository links should prefer the authors' or organization's official repository.

## Duplicate identity

Identity priority:

1. arXiv ID / DOI
2. paper-specific official identifier
3. normalized venue + normalized title

Generic conference/program identifiers are not paper identity.

## Cross-direction duplication

Important papers may appear in more than one direction. Cross-direction duplication is intentional when the paper plays a distinct technical role in each roadmap.

## Coverage states

- `SEARCHED`: a source/query was visited.
- `COVERED`: the required systematic route was completed for the current round.
- `SATURATED`: independent zero-new confirmation criteria have been met.

These terms must not be used interchangeably.

## Saturation

Venue and major-group coverage is not declared saturated merely because all entries were visited once. A non-zero round resets the zero-new saturation counter. Canonical one-hop/two-hop paper neighborhoods are also used to expose missed lineages.

## Public repository policy

The public repository stores metadata and links only. No paper PDF binaries and no private/internal discovery artifacts are committed.
