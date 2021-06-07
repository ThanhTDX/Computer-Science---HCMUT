
#include <stdlib.h>
#include "queue.h"
#include <pthread.h>

/* Remember to initilize the queue before using it */
void initialize_queue(struct pqueue_t * q) {
	q->head = q->tail = NULL;
<<<<<<< HEAD
	//pthread_mutex_init(&q->lock, NULL);
=======
	// pthread_mutex_init(&q->lock, NULL);
>>>>>>> 4158cf032e83da3565ad6ce4ae103fcb9e034c58
}

/* Return non-zero if the queue is empty */
int empty(struct pqueue_t * q) {
	return (q->head == NULL);
}

/* Get PCB of a process from the queue (q).
 * Return NULL if the queue is empty */
struct pcb_t * de_queue(struct pqueue_t * q) {
<<<<<<< HEAD
	struct pcb_t * proc = NULL;
	// TODO: return q->head->data and remember to update the queue's head
	// and tail if necessary. Remember to use 'lock' to avoid race
	// condition
	
	// YOUR CODE HERE

=======
	// pthread_mutex_lock(&q->lock);	
	
	if (!q->head) return NULL;
	struct pcb_t * proc = NULL;
	proc = q->head->data;
	// TODO: return q->head->data and remember to update the queue's head
	// and tail if necessary. Remember to use 'lock' to avoid race
	// condition
	static pthread_mutex_t dequeue = PTHREAD_MUTEX_INITIALIZER;

	struct qitem_t * tmp = q->head;
	q->head = tmp->next;
	free(tmp);
	tmp = NULL;
	if(q->head == NULL) q->tail = NULL;

	// pthread_mutex_unlock(&q->lock);	
>>>>>>> 4158cf032e83da3565ad6ce4ae103fcb9e034c58
	return proc;
}

/* Put PCB of a process to the queue. */
void en_queue(struct pqueue_t * q, struct pcb_t * proc) {
	// TODO: Update q->tail.
	// Remember to use 'lock' to avoid race condition
<<<<<<< HEAD
	
	// YOUR CODE HERE
	
=======

	// pthread_mutex_lock(&q->lock);
	// static pthread_mutex_t enqueue = PTHREAD_MUTEX_INITIALIZER;
	struct qitem_t *newItem = (struct qitem_t*) malloc(sizeof(struct qitem_t));
	newItem->data = proc;
	newItem->next = NULL;
	if (q->head == NULL) 
		q->head = newItem;
	else
		q->tail->next = newItem;
	q->tail = newItem;
	// pthread_mutex_unlock(&q->lock);
>>>>>>> 4158cf032e83da3565ad6ce4ae103fcb9e034c58
}


