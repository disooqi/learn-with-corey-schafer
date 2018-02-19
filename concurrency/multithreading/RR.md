```text
RULE 01: ALL shared resources SHALL be run in EXACTLY ONE thread. 
```


```text
RULE02: One category of sequencing problems is to make sure that step A and step B happen sequentially. The solution 
is to put both in the same thread where all actions proceed sequentially.
```


```text
RULE03: To implement a “barrier” that waits for parallel threads to complete, just join() all of the threads.
```

```text
RULE04: You can’t wait on daemon threads to complete (they are infinite loops). Instead, you join() on the queue itself. 
It waits until all the requested tasks are marked as being done.
```


```text
RULE05: Sometimes you need a global variable to communicate between functions. Global variables work great for this purpose in 
a single threaded program. In multi-threaded code, it mutable global state is a disaster. The better solution is to use 
a threading.local() that is global WITHIN a thread but not without.
```


```text
RULE06: Never try to kill a thread from something external to that thread. You never know if that thread is holding a lock. 
Python doesn’t provide a direct mechanism for kill threads externally; however, you can do it using ctypes, but that is 
a recipe for a deadlock.
```