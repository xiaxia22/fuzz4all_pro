# Class CountDownLatch

**Source:** `java.base\java\util\concurrent\CountDownLatch.html`

### Class Description

```java
public class
CountDownLatch

extends
Object
```

A synchronization aid that allows one or more threads to wait until
a set of operations being performed in other threads completes.

A

CountDownLatch

is initialized with a given

count

.
The

await

methods block until the current count reaches
zero due to invocations of the

countDown()

method, after which
all waiting threads are released and any subsequent invocations of

await

return immediately. This is a one-shot phenomenon
-- the count cannot be reset. If you need a version that resets the
count, consider using a

CyclicBarrier

.

A

CountDownLatch

is a versatile synchronization tool
and can be used for a number of purposes. A

CountDownLatch

initialized with a count of one serves as a
simple on/off latch, or gate: all threads invoking

await

wait at the gate until it is opened by a thread invoking

countDown()

. A

CountDownLatch

initialized to

N

can be used to make one thread wait until

N

threads have
completed some action, or some action has been completed N times.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

**Since:** 1.5

---

### Field Details

*No entries found.*

### Constructor Details

#### public CountDownLatch​(int count)

Constructs a

CountDownLatch

initialized with the given count.

**Parameters:**
- count

- the number of times

countDown()

must be invoked
before threads can pass through

await()

**Throws:**
- IllegalArgumentException

- if

count

is negative

---

### Method Details

#### public void await()
throws
InterruptedException

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

**Throws:**
- InterruptedException

- if the current thread is interrupted
while waiting

---

#### public boolean await​(long timeout,

TimeUnit
unit)
throws
InterruptedException

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the

timeout

argument

**Returns:**
- true

if the count reached zero and

false

if the waiting time elapsed before the count reached zero

**Throws:**
- InterruptedException

- if the current thread is interrupted
while waiting

---

#### public void countDown()

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

---

#### public long getCount()

Returns the current count.

This method is typically used for debugging and testing purposes.

**Returns:**
- the current count

---

#### public
String
toString()

Returns a string identifying this latch, as well as its state.
The state, in brackets, includes the String

"Count ="

followed by the current count.

**Overrides:**
- toString

in class

Object

**Returns:**
- a string identifying this latch, as well as its state

---

### Additional Sections

#### Class CountDownLatch

java.lang.Object

- java.util.concurrent.CountDownLatch

java.util.concurrent.CountDownLatch

```java
public class
CountDownLatch

extends
Object
```

A synchronization aid that allows one or more threads to wait until
a set of operations being performed in other threads completes.

A

CountDownLatch

is initialized with a given

count

.
The

await

methods block until the current count reaches
zero due to invocations of the

countDown()

method, after which
all waiting threads are released and any subsequent invocations of

await

return immediately. This is a one-shot phenomenon
-- the count cannot be reset. If you need a version that resets the
count, consider using a

CyclicBarrier

.

A

CountDownLatch

is a versatile synchronization tool
and can be used for a number of purposes. A

CountDownLatch

initialized with a count of one serves as a
simple on/off latch, or gate: all threads invoking

await

wait at the gate until it is opened by a thread invoking

countDown()

. A

CountDownLatch

initialized to

N

can be used to make one thread wait until

N

threads have
completed some action, or some action has been completed N times.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

**Since:** 1.5

public class

CountDownLatch

extends

Object

A synchronization aid that allows one or more threads to wait until
a set of operations being performed in other threads completes.

A

CountDownLatch

is initialized with a given

count

.
The

await

methods block until the current count reaches
zero due to invocations of the

countDown()

method, after which
all waiting threads are released and any subsequent invocations of

await

return immediately. This is a one-shot phenomenon
-- the count cannot be reset. If you need a version that resets the
count, consider using a

CyclicBarrier

.

A

CountDownLatch

is a versatile synchronization tool
and can be used for a number of purposes. A

CountDownLatch

initialized with a count of one serves as a
simple on/off latch, or gate: all threads invoking

await

wait at the gate until it is opened by a thread invoking

countDown()

. A

CountDownLatch

initialized to

N

can be used to make one thread wait until

N

threads have
completed some action, or some action has been completed N times.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

A

CountDownLatch

is initialized with a given

count

.
The

await

methods block until the current count reaches
zero due to invocations of the

countDown()

method, after which
all waiting threads are released and any subsequent invocations of

await

return immediately. This is a one-shot phenomenon
-- the count cannot be reset. If you need a version that resets the
count, consider using a

CyclicBarrier

.

A

CountDownLatch

is a versatile synchronization tool
and can be used for a number of purposes. A

CountDownLatch

initialized with a count of one serves as a
simple on/off latch, or gate: all threads invoking

await

wait at the gate until it is opened by a thread invoking

countDown()

. A

CountDownLatch

initialized to

N

can be used to make one thread wait until

N

threads have
completed some action, or some action has been completed N times.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

A

CountDownLatch

is a versatile synchronization tool
and can be used for a number of purposes. A

CountDownLatch

initialized with a count of one serves as a
simple on/off latch, or gate: all threads invoking

await

wait at the gate until it is opened by a thread invoking

countDown()

. A

CountDownLatch

initialized to

N

can be used to make one thread wait until

N

threads have
completed some action, or some action has been completed N times.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

A useful property of a

CountDownLatch

is that it
doesn't require that threads calling

countDown

wait for
the count to reach zero before proceeding, it simply prevents any
thread from proceeding past an

await

until all
threads could pass.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

Sample usage:

Here is a pair of classes in which a group
of worker threads use two countdown latches:

- The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

```java
class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

The first is a start signal that prevents any worker from proceeding
until the driver is ready for them to proceed;

The second is a completion signal that allows the driver to wait
until all workers have completed.

class Driver { // ...
void main() throws InterruptedException {
CountDownLatch startSignal = new CountDownLatch(1);
CountDownLatch doneSignal = new CountDownLatch(N);

for (int i = 0; i < N; ++i) // create and start threads
new Thread(new Worker(startSignal, doneSignal)).start();

doSomethingElse(); // don't let run yet
startSignal.countDown(); // let all threads proceed
doSomethingElse();
doneSignal.await(); // wait for all to finish
}
}

class Worker implements Runnable {
private final CountDownLatch startSignal;
private final CountDownLatch doneSignal;
Worker(CountDownLatch startSignal, CountDownLatch doneSignal) {
this.startSignal = startSignal;
this.doneSignal = doneSignal;
}
public void run() {
try {
startSignal.await();
doWork();
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}

Another typical usage would be to divide a problem into N parts,
describe each part with a Runnable that executes that portion and
counts down on the latch, and queue all the Runnables to an
Executor. When all sub-parts are complete, the coordinating thread
will be able to pass through await. (When threads must repeatedly
count down in this way, instead use a

CyclicBarrier

.)

```java
class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}
```

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

class Driver2 { // ...
void main() throws InterruptedException {
CountDownLatch doneSignal = new CountDownLatch(N);
Executor e = ...

for (int i = 0; i < N; ++i) // create and start threads
e.execute(new WorkerRunnable(doneSignal, i));

doneSignal.await(); // wait for all to finish
}
}

class WorkerRunnable implements Runnable {
private final CountDownLatch doneSignal;
private final int i;
WorkerRunnable(CountDownLatch doneSignal, int i) {
this.doneSignal = doneSignal;
this.i = i;
}
public void run() {
try {
doWork(i);
doneSignal.countDown();
} catch (InterruptedException ex) {} // return;
}

void doWork() { ... }
}

Memory consistency effects: Until the count reaches
zero, actions in a thread prior to calling

countDown()

happen-before

actions following a successful return from a corresponding

await()

in another thread.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CountDownLatch

​(int count)

Constructs a

CountDownLatch

initialized with the given count.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

await

()

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

boolean

await

​(long timeout,

TimeUnit

unit)

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

void

countDown

()

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

long

getCount

()

Returns the current count.

String

toString

()

Returns a string identifying this latch, as well as its state.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

Constructor Summary

Constructors

Constructor

Description

CountDownLatch

​(int count)

Constructs a

CountDownLatch

initialized with the given count.

---

#### Constructor Summary

Constructs a

CountDownLatch

initialized with the given count.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

await

()

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

boolean

await

​(long timeout,

TimeUnit

unit)

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

void

countDown

()

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

long

getCount

()

Returns the current count.

String

toString

()

Returns a string identifying this latch, as well as its state.

- Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Method Summary

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

Returns the current count.

Returns a string identifying this latch, as well as its state.

Methods declared in class java.lang.

Object

clone

,

equals

,

finalize

,

getClass

,

hashCode

,

notify

,

notifyAll

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- CountDownLatch

```java
public CountDownLatch​(int count)
```

Constructs a

CountDownLatch

initialized with the given count.

**Parameters:** count

- the number of times

countDown()

must be invoked
before threads can pass through

await()
**Throws:** IllegalArgumentException

- if

count

is negative

============ METHOD DETAIL ==========

- Method Detail

- await

```java
public void await()
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

- await

```java
public boolean await​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the count reached zero and

false

if the waiting time elapsed before the count reached zero
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

- countDown

```java
public void countDown()
```

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

- getCount

```java
public long getCount()
```

Returns the current count.

This method is typically used for debugging and testing purposes.

**Returns:** the current count

- toString

```java
public
String
toString()
```

Returns a string identifying this latch, as well as its state.
The state, in brackets, includes the String

"Count ="

followed by the current count.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this latch, as well as its state

Constructor Detail

- CountDownLatch

```java
public CountDownLatch​(int count)
```

Constructs a

CountDownLatch

initialized with the given count.

**Parameters:** count

- the number of times

countDown()

must be invoked
before threads can pass through

await()
**Throws:** IllegalArgumentException

- if

count

is negative

---

#### Constructor Detail

CountDownLatch

```java
public CountDownLatch​(int count)
```

Constructs a

CountDownLatch

initialized with the given count.

**Parameters:** count

- the number of times

countDown()

must be invoked
before threads can pass through

await()
**Throws:** IllegalArgumentException

- if

count

is negative

---

#### CountDownLatch

public CountDownLatch​(int count)

Constructs a

CountDownLatch

initialized with the given count.

Method Detail

- await

```java
public void await()
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

- await

```java
public boolean await​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the count reached zero and

false

if the waiting time elapsed before the count reached zero
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

- countDown

```java
public void countDown()
```

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

- getCount

```java
public long getCount()
```

Returns the current count.

This method is typically used for debugging and testing purposes.

**Returns:** the current count

- toString

```java
public
String
toString()
```

Returns a string identifying this latch, as well as its state.
The state, in brackets, includes the String

"Count ="

followed by the current count.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this latch, as well as its state

---

#### Method Detail

await

```java
public void await()
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

---

#### await

public void await()
throws

InterruptedException

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the current count is zero then this method returns immediately.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of two things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

await

```java
public boolean await​(long timeout,

TimeUnit
unit)
throws
InterruptedException
```

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the

timeout

argument
**Returns:** true

if the count reached zero and

false

if the waiting time elapsed before the count reached zero
**Throws:** InterruptedException

- if the current thread is interrupted
while waiting

---

#### await

public boolean await​(long timeout,

TimeUnit

unit)
throws

InterruptedException

Causes the current thread to wait until the latch has counted down to
zero, unless the thread is

interrupted

,
or the specified waiting time elapses.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

If the current count is zero then this method returns immediately
with the value

true

.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

If the current count is greater than zero then the current
thread becomes disabled for thread scheduling purposes and lies
dormant until one of three things happen:

- The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

The count reaches zero due to invocations of the

countDown()

method; or

Some other thread

interrupts

the current thread; or

The specified waiting time elapses.

If the count reaches zero then the method returns with the
value

true

.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

If the current thread:

- has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

then

InterruptedException

is thrown and the current thread's
interrupted status is cleared.

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

has its interrupted status set on entry to this method; or

is

interrupted

while waiting,

If the specified waiting time elapses then the value

false

is returned. If the time is less than or equal to zero, the method
will not wait at all.

countDown

```java
public void countDown()
```

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

---

#### countDown

public void countDown()

Decrements the count of the latch, releasing all waiting threads if
the count reaches zero.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

If the current count is greater than zero then it is decremented.
If the new count is zero then all waiting threads are re-enabled for
thread scheduling purposes.

If the current count equals zero then nothing happens.

If the current count equals zero then nothing happens.

getCount

```java
public long getCount()
```

Returns the current count.

This method is typically used for debugging and testing purposes.

**Returns:** the current count

---

#### getCount

public long getCount()

Returns the current count.

This method is typically used for debugging and testing purposes.

This method is typically used for debugging and testing purposes.

toString

```java
public
String
toString()
```

Returns a string identifying this latch, as well as its state.
The state, in brackets, includes the String

"Count ="

followed by the current count.

**Overrides:** toString

in class

Object
**Returns:** a string identifying this latch, as well as its state

---

#### toString

public

String

toString()

Returns a string identifying this latch, as well as its state.
The state, in brackets, includes the String

"Count ="

followed by the current count.

---

