0x03. Caching


Page fault: a Type of exception raised by computer Hardware when a running process acess a memory page that currently not mapped to the memory management unit .

Least Recently Used(LRU) algorithm:

1. Check if the requested page is present on the page frame
2. If not, place that page and that's a page fault
3. if the requested page is already present on the page frame, that's a hit .(We do nothing)


least recently used  
<-------------------  

| 7 	| 0 	| 1 	| 2 	| 0 	| 3 	| 0 	| 4 	|
|---	|---	|---	|---	|---	|---	|---	|---	|
| 7 	| 7 	| 7 	| 2 	| 2 	| 2 	| 2 	| 4 	|
|   	| 0 	| 0 	| 0 	| 0 	| 0 	| 0 	| 0 	|
|   	|   	| 1 	| 1 	| 1 	| 3 	| 3 	| 3 	|



F F F F * F * F
* Page hit .
==> drawbacks: overhead: we need to keep track of pages(when they have been added)
==> Difficult to implement
