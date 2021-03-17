0x02-python_async_comprehension

Project Description:
In this prototype, we simulate an I/O stream of data, that take 10 seconds to finish data transmission.
This stream of data is represented with a loop that iterate 10 times , with a delay of 1 second for each iteration.
--> Each eteration take one second and return a random floated number

task [0]: Data is collected using an async generator function returning a generator object(iterator)
task [1]: the returned iterator from the async generator function, is used inside an async comprehensing ,
          --> resulting a list.
task [2]: We run 4 different stream concurrrently(using the async comprehensing previously created) .
        --> it took only 10 second roughly to get the data from the 4 streams (I/O).
        insted of 40 seconds(in case of sychronous code).
