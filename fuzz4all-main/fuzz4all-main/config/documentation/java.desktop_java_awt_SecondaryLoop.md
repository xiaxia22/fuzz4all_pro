# Interface SecondaryLoop

**Source:** `java.desktop\java\awt\SecondaryLoop.html`

### Class Description

```java
public interface
SecondaryLoop
```

A helper interface to run the nested event loop.

Objects that implement this interface are created with the

EventQueue.createSecondaryLoop()

method. The interface
provides two methods,

enter()

and

exit()

,
which can be used to start and stop the event loop.

When the

enter()

method is called, the current
thread is blocked until the loop is terminated by the

exit()

method. Also, a new event loop is started
on the event dispatch thread, which may or may not be
the current thread. The loop can be terminated on any
thread by calling its

exit()

method. After the
loop is terminated, the

SecondaryLoop

object can
be reused to run a new nested event loop.

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

**Since:** 1.7
**See Also:** Dialog.show()

,

EventQueue.createSecondaryLoop()

,

Toolkit.getSystemEventQueue()

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean enter()

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

**Returns:**
- true

after termination of the secondary loop,
if the secondary loop was started by this call,

false

otherwise

---

#### boolean exit()

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

**Returns:**
- true

if this loop was previously started and
has not yet been finished with the

exit()

method,

false

otherwise

---

### Additional Sections

#### Interface SecondaryLoop

```java
public interface
SecondaryLoop
```

A helper interface to run the nested event loop.

Objects that implement this interface are created with the

EventQueue.createSecondaryLoop()

method. The interface
provides two methods,

enter()

and

exit()

,
which can be used to start and stop the event loop.

When the

enter()

method is called, the current
thread is blocked until the loop is terminated by the

exit()

method. Also, a new event loop is started
on the event dispatch thread, which may or may not be
the current thread. The loop can be terminated on any
thread by calling its

exit()

method. After the
loop is terminated, the

SecondaryLoop

object can
be reused to run a new nested event loop.

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

**Since:** 1.7
**See Also:** Dialog.show()

,

EventQueue.createSecondaryLoop()

,

Toolkit.getSystemEventQueue()

public interface

SecondaryLoop

A helper interface to run the nested event loop.

Objects that implement this interface are created with the

EventQueue.createSecondaryLoop()

method. The interface
provides two methods,

enter()

and

exit()

,
which can be used to start and stop the event loop.

When the

enter()

method is called, the current
thread is blocked until the loop is terminated by the

exit()

method. Also, a new event loop is started
on the event dispatch thread, which may or may not be
the current thread. The loop can be terminated on any
thread by calling its

exit()

method. After the
loop is terminated, the

SecondaryLoop

object can
be reused to run a new nested event loop.

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

Objects that implement this interface are created with the

EventQueue.createSecondaryLoop()

method. The interface
provides two methods,

enter()

and

exit()

,
which can be used to start and stop the event loop.

When the

enter()

method is called, the current
thread is blocked until the loop is terminated by the

exit()

method. Also, a new event loop is started
on the event dispatch thread, which may or may not be
the current thread. The loop can be terminated on any
thread by calling its

exit()

method. After the
loop is terminated, the

SecondaryLoop

object can
be reused to run a new nested event loop.

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

When the

enter()

method is called, the current
thread is blocked until the loop is terminated by the

exit()

method. Also, a new event loop is started
on the event dispatch thread, which may or may not be
the current thread. The loop can be terminated on any
thread by calling its

exit()

method. After the
loop is terminated, the

SecondaryLoop

object can
be reused to run a new nested event loop.

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

A typical use case of applying this interface is AWT
and Swing modal dialogs. When a modal dialog is shown on
the event dispatch thread, it enters a new secondary loop.
Later, when the dialog is hidden or disposed, it exits
the loop, and the thread continues its execution.

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

The following example illustrates a simple use case of
secondary loops:

```java
SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}
```

SecondaryLoop loop;

JButton jButton = new JButton("Button");
jButton.addActionListener(new ActionListener() {

@Override

public void actionPerformed(ActionEvent e) {
Toolkit tk = Toolkit.getDefaultToolkit();
EventQueue eq = tk.getSystemEventQueue();
loop = eq.createSecondaryLoop();

// Spawn a new thread to do the work
Thread worker = new WorkerThread();
worker.start();

// Enter the loop to block the current event
// handler, but leave UI responsive
if (!loop.enter()) {
// Report an error
}
}
});

class WorkerThread extends Thread {

@Override

public void run() {
// Perform calculations
doSomethingUseful();

// Exit the loop
loop.exit();
}
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

enter

()

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

boolean

exit

()

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

enter

()

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

boolean

exit

()

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

---

#### Method Summary

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

============ METHOD DETAIL ==========

- Method Detail

- enter

```java
boolean enter()
```

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

**Returns:** true

after termination of the secondary loop,
if the secondary loop was started by this call,

false

otherwise

- exit

```java
boolean exit()
```

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

**Returns:** true

if this loop was previously started and
has not yet been finished with the

exit()

method,

false

otherwise

Method Detail

- enter

```java
boolean enter()
```

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

**Returns:** true

after termination of the secondary loop,
if the secondary loop was started by this call,

false

otherwise

- exit

```java
boolean exit()
```

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

**Returns:** true

if this loop was previously started and
has not yet been finished with the

exit()

method,

false

otherwise

---

#### Method Detail

enter

```java
boolean enter()
```

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

**Returns:** true

after termination of the secondary loop,
if the secondary loop was started by this call,

false

otherwise

---

#### enter

boolean enter()

Blocks the execution of the current thread and enters a new
secondary event loop on the event dispatch thread.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

This method can be called by any thread including the event
dispatch thread. This thread will be blocked until the

exit()

method is called or the loop is terminated. A new
secondary loop will be created on the event dispatch thread
for dispatching events in either case.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

This method can only start one new event loop at a time per
object. If a secondary event loop has already been started
by this object and is currently still running, this method
returns

false

to indicate that it was not successful
in starting a new event loop. Otherwise, this method blocks
the calling thread and later returns

true

when the
new event loop is terminated. At such time, this object can
again be used to start another new event loop.

exit

```java
boolean exit()
```

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

**Returns:** true

if this loop was previously started and
has not yet been finished with the

exit()

method,

false

otherwise

---

#### exit

boolean exit()

Unblocks the execution of the thread blocked by the

enter()

method and exits the secondary loop.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

This method resumes the thread that called the

enter()

method and exits the secondary loop that was created when
the

enter()

method was invoked.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

Note that if any other secondary loop is started while this
loop is running, the blocked thread will not resume execution
until the nested loop is terminated.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

If this secondary loop has not been started with the

enter()

method, or this secondary loop has already finished
with the

exit()

method, this method returns

false

, otherwise

true

is returned.

---

