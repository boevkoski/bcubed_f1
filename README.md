# BCubed F1
### Implementation of the BCubed F1 score for measuring similarity of two community detection partitions.

The BCubed measure was originally proposed to evaluate effectiveness of document clustering [paper](https://citeseerx.ist.psu.edu/viewdoc/download?doi=10.1.1.47.5848&rep=rep1&type=pdf).
Its properties were compared to a wide range of other extrinsic clustering evaluation metrics,
with the [conclusion](https://link.springer.com/content/pdf/10.1007/s10791-008-9066-8.pdf) that BCubed satisfies all the required qualitative properties~\cite{Amigo2009bcubed}.
Since data clustering and community detection in networks produce analogous results,
one can also apply the BCubed measure to evaluate the detected communities.

The F1 is calculated node-wise as a sum of the Precision and Recall of individual nodes. As the Precision and Recall are normalized by the number of nodes in the network, the F1 ranges from 0 (no similarity between the partitions) to 1 (complete match between the partitions). A detailed definition of the Bcubed F1 metric for communities, including the general form for non-identical node sets, can be found in this [work](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0256175).

