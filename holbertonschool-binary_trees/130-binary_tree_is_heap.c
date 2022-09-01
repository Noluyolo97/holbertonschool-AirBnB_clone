#include "binary_trees.h"


/**
 * countNodes - This function counts the number of nodes in a binary tree
 * @root: pointer to the tree to be counted
 * Return: Number of total nodes in tree, 0 if NULL
 */

unsigned int countNodes(const binary_tree_t *root)
{
	if (root == NULL)
		return (0);

	return (1 + countNodes(root->left) + countNodes(root->right));
}

/**
 * isCompleteUtil - This function checks if the binary tree is complete or not
 * @root: pointer to the tree to be checked
 * @index: unsigned int that helps assign an index to each node
 * @number_nodes: unsigned int that returns total number of nodes in the tree
 * Return: 1 if binary tree is complete, 0 otherwise
 */

int isCompleteUtil(const binary_tree_t *root, unsigned int index,
		    unsigned int number_nodes)
{

	if (root == NULL)
		return (1);

	if (index >= number_nodes)
		return (0);

	return (isCompleteUtil(root->left, 2 * index + 1, number_nodes) &&
		isCompleteUtil(root->right, 2 * index + 2, number_nodes));
}


/**
 * isHeapUtil - Main utility function checks the heap property of a tree.
 * @root: pointer to the tree to be checked
 * Return: 1 if tree is a max binary heap, 0 if not
 */

int isHeapUtil(const binary_tree_t *root)
{
	if (root->left == NULL && root->right == NULL)
		return (1);


	if (root->right == NULL)
	{

		return (root->n >= root->left->n);
	}
	else
	{
		if (root->n >= root->left->n &&
		    root->n >= root->right->n)
			return ((isHeapUtil(root->left)) &&
				(isHeapUtil(root->right)));
		else
			return (0);
	}
}

/**
 * binary_tree_is_heap - function that checks if a binary tree is a valid Max
 * Binary Heap
 * https://www.geeksforgeeks.org/check-if-a-given-binary-tree-is-heap/
 * @tree: pointer to the tree to be checked
 * Return: 1 if tree is a max binary heap, 0 if not
 */


int binary_tree_is_heap(const binary_tree_t *tree)
{
	unsigned int node_count = countNodes(tree);
	unsigned int index = 0;

	if (tree == NULL)
		return (0);

	if (isCompleteUtil(tree, index, node_count) && isHeapUtil(tree))
		return (1);
	return (0);
}
