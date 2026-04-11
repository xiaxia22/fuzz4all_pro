# Class SwingWorker<T,​V>

**Source:** `java.desktop\javax\swing\SwingWorker.html`

### Class Description

```java
public abstract class
SwingWorker<T,​V>

extends
Object

implements
RunnableFuture
<T>
```

An abstract class to perform lengthy GUI-interaction tasks in a
background thread. Several background threads can be used to execute such
tasks. However, the exact strategy of choosing a thread for any particular

SwingWorker

is unspecified and should not be relied on.

When writing a multi-threaded application using Swing, there are
two constraints to keep in mind:
(refer to

Concurrency in Swing

for more details):

- Time-consuming tasks should not be run on the

Event
Dispatch Thread

. Otherwise the application becomes unresponsive.
- Swing components should be accessed on the

Event
Dispatch Thread

only.

These constraints mean that a GUI application with time intensive
computing needs at least two threads: 1) a thread to perform the lengthy
task and 2) the

Event Dispatch Thread

(EDT) for all GUI-related
activities. This involves inter-thread communication which can be
tricky to implement.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

**Type Parameters:** T

- the result type returned by this

SwingWorker's

doInBackground

and

get

methods
**Type Parameters:** V

- the type used for carrying out intermediate results by this

SwingWorker's

publish

and

process

methods

---

### Field Details

*No entries found.*

### Constructor Details

#### public SwingWorker()

Constructs this

SwingWorker

.

---

### Method Details

#### protected abstract
T
doInBackground()
throws
Exception

Computes a result, or throws an exception if unable to do so.

Note that this method is executed only once.

Note: this method is executed in a background thread.

**Returns:**
- the computed result

**Throws:**
- Exception

- if unable to compute a result

---

#### public final void run()

Sets this

Future

to the result of computation unless
it has been cancelled.

**Specified by:**
- run

in interface

Runnable
- run

in interface

RunnableFuture

<

T

>

**See Also:**
- Thread.run()

---

#### @SafeVarargs

protected final void publish​(
V
... chunks)

Sends data chunks to the

process(java.util.List<V>)

method. This method is to be
used from inside the

doInBackground

method to deliver
intermediate results
for processing on the

Event Dispatch Thread

inside the

process

method.

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

**Parameters:**
- chunks

- intermediate results to process

**See Also:**
- process(java.util.List<V>)

---

#### protected void process​(
List
<
V
> chunks)

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Please refer to the

publish(V...)

method for more details.

**Parameters:**
- chunks

- intermediate results to process

**See Also:**
- publish(V...)

---

#### protected void done()

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished. The default
implementation does nothing. Subclasses may override this method to
perform completion actions on the

Event Dispatch Thread

. Note
that you can query status inside the implementation of this method to
determine the result of this task or whether this task has been cancelled.

**See Also:**
- doInBackground()

,

Future.isCancelled()

,

get()

---

#### protected final void setProgress​(int progress)

Sets the

progress

bound property.
The value should be from 0 to 100.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

**Parameters:**
- progress

- the progress value to set

**Throws:**
- IllegalArgumentException

- is value not from 0 to 100

---

#### public final int getProgress()

Returns the

progress

bound property.

**Returns:**
- the progress bound property.

---

#### public final void execute()

Schedules this

SwingWorker

for execution on a

worker

thread. There are a number of

worker

threads available. In the
event all

worker

threads are busy handling other

SwingWorkers

this

SwingWorker

is placed in a waiting
queue.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

---

#### public final
T
get()
throws
InterruptedException
,

ExecutionException

Waits if necessary for the computation to complete, and then
retrieves its result.

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

**Specified by:**
- get

in interface

Future

<

T

>

**Returns:**
- the computed result

**Throws:**
- CancellationException

- if the computation was cancelled
- InterruptedException

- if the current thread was interrupted
while waiting
- ExecutionException

- if the computation threw an
exception

---

#### public final
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Please refer to

get()

for more details.

**Specified by:**
- get

in interface

Future

<

T

>

**Parameters:**
- timeout

- the maximum time to wait
- unit

- the time unit of the timeout argument

**Returns:**
- the computed result

**Throws:**
- CancellationException

- if the computation was cancelled
- InterruptedException

- if the current thread was interrupted
while waiting
- ExecutionException

- if the computation threw an
exception
- TimeoutException

- if the wait timed out

---

#### public final void addPropertyChangeListener​(
PropertyChangeListener
listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all properties. The same listener object may be added
more than once, and will be called as many times as it is added. If

listener

is

null

, no exception is thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:**
- listener

- the

PropertyChangeListener

to be added

---

#### public final void removePropertyChangeListener​(
PropertyChangeListener
listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:**
- listener

- the

PropertyChangeListener

to be removed

---

#### public final void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)

Reports a bound property update to any registered listeners. No event is
fired if

old

and

new

are equal and non-null.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:**
- propertyName

- the programmatic name of the property that was
changed
- oldValue

- the old value of the property
- newValue

- the new value of the property

---

#### public final
PropertyChangeSupport
getPropertyChangeSupport()

Returns the

PropertyChangeSupport

for this

SwingWorker

.
This method is used when flexible access to bound properties support is
needed.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

**Returns:**
- PropertyChangeSupport

for this

SwingWorker

---

#### public final
SwingWorker.StateValue
getState()

Returns the

SwingWorker

state bound property.

**Returns:**
- the current state

---

### Additional Sections

#### Class SwingWorker<T,​V>

java.lang.Object

- javax.swing.SwingWorker<T,​V>

javax.swing.SwingWorker<T,​V>

**Type Parameters:** T

- the result type returned by this

SwingWorker's

doInBackground

and

get

methods
**Type Parameters:** V

- the type used for carrying out intermediate results by this

SwingWorker's

publish

and

process

methods

**All Implemented Interfaces:** Runnable

,

Future

<T>

,

RunnableFuture

<T>

```java
public abstract class
SwingWorker<T,​V>

extends
Object

implements
RunnableFuture
<T>
```

An abstract class to perform lengthy GUI-interaction tasks in a
background thread. Several background threads can be used to execute such
tasks. However, the exact strategy of choosing a thread for any particular

SwingWorker

is unspecified and should not be relied on.

When writing a multi-threaded application using Swing, there are
two constraints to keep in mind:
(refer to

Concurrency in Swing

for more details):

- Time-consuming tasks should not be run on the

Event
Dispatch Thread

. Otherwise the application becomes unresponsive.
- Swing components should be accessed on the

Event
Dispatch Thread

only.

These constraints mean that a GUI application with time intensive
computing needs at least two threads: 1) a thread to perform the lengthy
task and 2) the

Event Dispatch Thread

(EDT) for all GUI-related
activities. This involves inter-thread communication which can be
tricky to implement.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

**Since:** 1.6

public abstract class

SwingWorker<T,​V>

extends

Object

implements

RunnableFuture

<T>

An abstract class to perform lengthy GUI-interaction tasks in a
background thread. Several background threads can be used to execute such
tasks. However, the exact strategy of choosing a thread for any particular

SwingWorker

is unspecified and should not be relied on.

When writing a multi-threaded application using Swing, there are
two constraints to keep in mind:
(refer to

Concurrency in Swing

for more details):

- Time-consuming tasks should not be run on the

Event
Dispatch Thread

. Otherwise the application becomes unresponsive.
- Swing components should be accessed on the

Event
Dispatch Thread

only.

These constraints mean that a GUI application with time intensive
computing needs at least two threads: 1) a thread to perform the lengthy
task and 2) the

Event Dispatch Thread

(EDT) for all GUI-related
activities. This involves inter-thread communication which can be
tricky to implement.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

When writing a multi-threaded application using Swing, there are
two constraints to keep in mind:
(refer to

Concurrency in Swing

for more details):

- Time-consuming tasks should not be run on the

Event
Dispatch Thread

. Otherwise the application becomes unresponsive.
- Swing components should be accessed on the

Event
Dispatch Thread

only.

These constraints mean that a GUI application with time intensive
computing needs at least two threads: 1) a thread to perform the lengthy
task and 2) the

Event Dispatch Thread

(EDT) for all GUI-related
activities. This involves inter-thread communication which can be
tricky to implement.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Time-consuming tasks should not be run on the

Event
Dispatch Thread

. Otherwise the application becomes unresponsive.

Swing components should be accessed on the

Event
Dispatch Thread

only.

These constraints mean that a GUI application with time intensive
computing needs at least two threads: 1) a thread to perform the lengthy
task and 2) the

Event Dispatch Thread

(EDT) for all GUI-related
activities. This involves inter-thread communication which can be
tricky to implement.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

SwingWorker

is designed for situations where you need to have a long
running task run in a background thread and provide updates to the UI
either when done, or while processing.
Subclasses of

SwingWorker

must implement
the

doInBackground()

method to perform the background computation.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Workflow

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

There are three threads involved in the life cycle of a

SwingWorker

:

- Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Current

thread: The

execute()

method is
called on this thread. It schedules

SwingWorker

for the execution on a

worker

thread and returns immediately. One can wait for the

SwingWorker

to
complete using the

get

methods.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Worker

thread: The

doInBackground()

method is called on this thread.
This is where all background activities should happen. To notify

PropertyChangeListeners

about bound properties changes use the

firePropertyChange

and

getPropertyChangeSupport()

methods. By default there are two bound
properties available:

state

and

progress

.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Event Dispatch Thread

: All Swing related activities occur
on this thread.

SwingWorker

invokes the

process

and

done()

methods and notifies
any

PropertyChangeListeners

on this thread.

Often, the

Current

thread is the

Event Dispatch
Thread

.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Before the

doInBackground

method is invoked on a

worker

thread,

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.STARTED

. After the

doInBackground

method is finished the

done

method is
executed. Then

SwingWorker

notifies any

PropertyChangeListeners

about the

state

property change to

StateValue.DONE

.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Sample Usage

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

The following example illustrates the simplest use case. Some
processing is done in the background and when done you update a Swing
component.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Say we want to find the "Meaning of Life" and display the result in
a

JLabel

.

```java
final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();
```

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

final JLabel label;
class MeaningOfLifeFinder extends SwingWorker<String, Object> {

@Override

public String doInBackground() {
return findTheMeaningOfLife();
}

@Override

protected void done() {
try {
label.setText(get());
} catch (Exception ignore) {
}
}
}

(new MeaningOfLifeFinder()).execute();

The next example is useful in situations where you wish to process data
as it is ready on the

Event Dispatch Thread

.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

Now we want to find the first N prime numbers and display the results in a

JTextArea

. While this is computing, we want to update our
progress in a

JProgressBar

. Finally, we also want to print
the prime numbers to

System.out

.

```java
class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got
```

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

class PrimeNumbersTask extends
SwingWorker<List<Integer>, Integer> {
PrimeNumbersTask(JTextArea textArea, int numbersToFind) {
//initialize
}

@Override

public List<Integer> doInBackground() {
while (! enough && ! isCancelled()) {
number = nextPrimeNumber();
publish(number);
setProgress(100 * numbers.size() / numbersToFind);
}
}
return numbers;
}

@Override

protected void process(List<Integer> chunks) {
for (int number : chunks) {
textArea.append(number + "\n");
}
}
}

JTextArea textArea = new JTextArea();
final JProgressBar progressBar = new JProgressBar(0, 100);
PrimeNumbersTask task = new PrimeNumbersTask(textArea, N);
task.addPropertyChangeListener(
new PropertyChangeListener() {
public void propertyChange(PropertyChangeEvent evt) {
if ("progress".equals(evt.getPropertyName())) {
progressBar.setValue((Integer)evt.getNewValue());
}
}
});

task.execute();
System.out.println(task.get()); //prints all prime numbers we have got

Because

SwingWorker

implements

Runnable

, a

SwingWorker

can be submitted to an

Executor

for execution.

======== NESTED CLASS SUMMARY ========

- Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SwingWorker.StateValue

Values for the

state

bound property.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SwingWorker

()

Constructs this

SwingWorker

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

protected abstract

T

doInBackground

()

Computes a result, or throws an exception if unable to do so.

protected void

done

()

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished.

void

execute

()

Schedules this

SwingWorker

for execution on a

worker

thread.

void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Reports a bound property update to any registered listeners.

T

get

()

Waits if necessary for the computation to complete, and then
retrieves its result.

T

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

int

getProgress

()

Returns the

progress

bound property.

PropertyChangeSupport

getPropertyChangeSupport

()

Returns the

PropertyChangeSupport

for this

SwingWorker

.

SwingWorker.StateValue

getState

()

Returns the

SwingWorker

state bound property.

protected void

process

​(

List

<

V

> chunks)

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

protected void

publish

​(

V

... chunks)

Sends data chunks to the

process(java.util.List<V>)

method.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

run

()

Sets this

Future

to the result of computation unless
it has been cancelled.

protected void

setProgress

​(int progress)

Sets the

progress

bound property.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.concurrent.

Future

cancel

,

isCancelled

,

isDone

Nested Class Summary

Nested Classes

Modifier and Type

Class

Description

static class

SwingWorker.StateValue

Values for the

state

bound property.

---

#### Nested Class Summary

Values for the

state

bound property.

Constructor Summary

Constructors

Constructor

Description

SwingWorker

()

Constructs this

SwingWorker

.

---

#### Constructor Summary

Constructs this

SwingWorker

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Concrete Methods

Modifier and Type

Method

Description

void

addPropertyChangeListener

​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list.

protected abstract

T

doInBackground

()

Computes a result, or throws an exception if unable to do so.

protected void

done

()

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished.

void

execute

()

Schedules this

SwingWorker

for execution on a

worker

thread.

void

firePropertyChange

​(

String

propertyName,

Object

oldValue,

Object

newValue)

Reports a bound property update to any registered listeners.

T

get

()

Waits if necessary for the computation to complete, and then
retrieves its result.

T

get

​(long timeout,

TimeUnit

unit)

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

int

getProgress

()

Returns the

progress

bound property.

PropertyChangeSupport

getPropertyChangeSupport

()

Returns the

PropertyChangeSupport

for this

SwingWorker

.

SwingWorker.StateValue

getState

()

Returns the

SwingWorker

state bound property.

protected void

process

​(

List

<

V

> chunks)

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

protected void

publish

​(

V

... chunks)

Sends data chunks to the

process(java.util.List<V>)

method.

void

removePropertyChangeListener

​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list.

void

run

()

Sets this

Future

to the result of computation unless
it has been cancelled.

protected void

setProgress

​(int progress)

Sets the

progress

bound property.

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

toString

,

wait

,

wait

,

wait

- Methods declared in interface java.util.concurrent.

Future

cancel

,

isCancelled

,

isDone

---

#### Method Summary

Adds a

PropertyChangeListener

to the listener list.

Computes a result, or throws an exception if unable to do so.

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished.

Schedules this

SwingWorker

for execution on a

worker

thread.

Reports a bound property update to any registered listeners.

Waits if necessary for the computation to complete, and then
retrieves its result.

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Returns the

progress

bound property.

Returns the

PropertyChangeSupport

for this

SwingWorker

.

Returns the

SwingWorker

state bound property.

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Sends data chunks to the

process(java.util.List<V>)

method.

Removes a

PropertyChangeListener

from the listener list.

Sets this

Future

to the result of computation unless
it has been cancelled.

Sets the

progress

bound property.

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

toString

,

wait

,

wait

,

wait

---

#### Methods declared in class java.lang. Object

Methods declared in interface java.util.concurrent.

Future

cancel

,

isCancelled

,

isDone

---

#### Methods declared in interface java.util.concurrent. Future

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SwingWorker

```java
public SwingWorker()
```

Constructs this

SwingWorker

.

============ METHOD DETAIL ==========

- Method Detail

- doInBackground

```java
protected abstract
T
doInBackground()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

Note that this method is executed only once.

Note: this method is executed in a background thread.

**Returns:** the computed result
**Throws:** Exception

- if unable to compute a result

- run

```java
public final void run()
```

Sets this

Future

to the result of computation unless
it has been cancelled.

**Specified by:** run

in interface

Runnable
**Specified by:** run

in interface

RunnableFuture

<

T

>
**See Also:** Thread.run()

- publish

```java
@SafeVarargs

protected final void publish​(
V
... chunks)
```

Sends data chunks to the

process(java.util.List<V>)

method. This method is to be
used from inside the

doInBackground

method to deliver
intermediate results
for processing on the

Event Dispatch Thread

inside the

process

method.

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

**Parameters:** chunks

- intermediate results to process
**See Also:** process(java.util.List<V>)

- process

```java
protected void process​(
List
<
V
> chunks)
```

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Please refer to the

publish(V...)

method for more details.

**Parameters:** chunks

- intermediate results to process
**See Also:** publish(V...)

- done

```java
protected void done()
```

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished. The default
implementation does nothing. Subclasses may override this method to
perform completion actions on the

Event Dispatch Thread

. Note
that you can query status inside the implementation of this method to
determine the result of this task or whether this task has been cancelled.

**See Also:** doInBackground()

,

Future.isCancelled()

,

get()

- setProgress

```java
protected final void setProgress​(int progress)
```

Sets the

progress

bound property.
The value should be from 0 to 100.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

**Parameters:** progress

- the progress value to set
**Throws:** IllegalArgumentException

- is value not from 0 to 100

- getProgress

```java
public final int getProgress()
```

Returns the

progress

bound property.

**Returns:** the progress bound property.

- execute

```java
public final void execute()
```

Schedules this

SwingWorker

for execution on a

worker

thread. There are a number of

worker

threads available. In the
event all

worker

threads are busy handling other

SwingWorkers

this

SwingWorker

is placed in a waiting
queue.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

- get

```java
public final
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

- get

```java
public final
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Please refer to

get()

for more details.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

- addPropertyChangeListener

```java
public final void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all properties. The same listener object may be added
more than once, and will be called as many times as it is added. If

listener

is

null

, no exception is thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be added

- removePropertyChangeListener

```java
public final void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

- firePropertyChange

```java
public final void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Reports a bound property update to any registered listeners. No event is
fired if

old

and

new

are equal and non-null.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** propertyName

- the programmatic name of the property that was
changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

- getPropertyChangeSupport

```java
public final
PropertyChangeSupport
getPropertyChangeSupport()
```

Returns the

PropertyChangeSupport

for this

SwingWorker

.
This method is used when flexible access to bound properties support is
needed.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

**Returns:** PropertyChangeSupport

for this

SwingWorker

- getState

```java
public final
SwingWorker.StateValue
getState()
```

Returns the

SwingWorker

state bound property.

**Returns:** the current state

Constructor Detail

- SwingWorker

```java
public SwingWorker()
```

Constructs this

SwingWorker

.

---

#### Constructor Detail

SwingWorker

```java
public SwingWorker()
```

Constructs this

SwingWorker

.

---

#### SwingWorker

public SwingWorker()

Constructs this

SwingWorker

.

Method Detail

- doInBackground

```java
protected abstract
T
doInBackground()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

Note that this method is executed only once.

Note: this method is executed in a background thread.

**Returns:** the computed result
**Throws:** Exception

- if unable to compute a result

- run

```java
public final void run()
```

Sets this

Future

to the result of computation unless
it has been cancelled.

**Specified by:** run

in interface

Runnable
**Specified by:** run

in interface

RunnableFuture

<

T

>
**See Also:** Thread.run()

- publish

```java
@SafeVarargs

protected final void publish​(
V
... chunks)
```

Sends data chunks to the

process(java.util.List<V>)

method. This method is to be
used from inside the

doInBackground

method to deliver
intermediate results
for processing on the

Event Dispatch Thread

inside the

process

method.

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

**Parameters:** chunks

- intermediate results to process
**See Also:** process(java.util.List<V>)

- process

```java
protected void process​(
List
<
V
> chunks)
```

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Please refer to the

publish(V...)

method for more details.

**Parameters:** chunks

- intermediate results to process
**See Also:** publish(V...)

- done

```java
protected void done()
```

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished. The default
implementation does nothing. Subclasses may override this method to
perform completion actions on the

Event Dispatch Thread

. Note
that you can query status inside the implementation of this method to
determine the result of this task or whether this task has been cancelled.

**See Also:** doInBackground()

,

Future.isCancelled()

,

get()

- setProgress

```java
protected final void setProgress​(int progress)
```

Sets the

progress

bound property.
The value should be from 0 to 100.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

**Parameters:** progress

- the progress value to set
**Throws:** IllegalArgumentException

- is value not from 0 to 100

- getProgress

```java
public final int getProgress()
```

Returns the

progress

bound property.

**Returns:** the progress bound property.

- execute

```java
public final void execute()
```

Schedules this

SwingWorker

for execution on a

worker

thread. There are a number of

worker

threads available. In the
event all

worker

threads are busy handling other

SwingWorkers

this

SwingWorker

is placed in a waiting
queue.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

- get

```java
public final
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

- get

```java
public final
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Please refer to

get()

for more details.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

- addPropertyChangeListener

```java
public final void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all properties. The same listener object may be added
more than once, and will be called as many times as it is added. If

listener

is

null

, no exception is thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be added

- removePropertyChangeListener

```java
public final void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

- firePropertyChange

```java
public final void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Reports a bound property update to any registered listeners. No event is
fired if

old

and

new

are equal and non-null.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** propertyName

- the programmatic name of the property that was
changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

- getPropertyChangeSupport

```java
public final
PropertyChangeSupport
getPropertyChangeSupport()
```

Returns the

PropertyChangeSupport

for this

SwingWorker

.
This method is used when flexible access to bound properties support is
needed.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

**Returns:** PropertyChangeSupport

for this

SwingWorker

- getState

```java
public final
SwingWorker.StateValue
getState()
```

Returns the

SwingWorker

state bound property.

**Returns:** the current state

---

#### Method Detail

doInBackground

```java
protected abstract
T
doInBackground()
throws
Exception
```

Computes a result, or throws an exception if unable to do so.

Note that this method is executed only once.

Note: this method is executed in a background thread.

**Returns:** the computed result
**Throws:** Exception

- if unable to compute a result

---

#### doInBackground

protected abstract

T

doInBackground()
throws

Exception

Computes a result, or throws an exception if unable to do so.

Note that this method is executed only once.

Note: this method is executed in a background thread.

Note that this method is executed only once.

Note: this method is executed in a background thread.

Note: this method is executed in a background thread.

run

```java
public final void run()
```

Sets this

Future

to the result of computation unless
it has been cancelled.

**Specified by:** run

in interface

Runnable
**Specified by:** run

in interface

RunnableFuture

<

T

>
**See Also:** Thread.run()

---

#### run

public final void run()

Sets this

Future

to the result of computation unless
it has been cancelled.

publish

```java
@SafeVarargs

protected final void publish​(
V
... chunks)
```

Sends data chunks to the

process(java.util.List<V>)

method. This method is to be
used from inside the

doInBackground

method to deliver
intermediate results
for processing on the

Event Dispatch Thread

inside the

process

method.

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

**Parameters:** chunks

- intermediate results to process
**See Also:** process(java.util.List<V>)

---

#### publish

@SafeVarargs

protected final void publish​(

V

... chunks)

Sends data chunks to the

process(java.util.List<V>)

method. This method is to be
used from inside the

doInBackground

method to deliver
intermediate results
for processing on the

Event Dispatch Thread

inside the

process

method.

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

Because the

process

method is invoked asynchronously on
the

Event Dispatch Thread

multiple invocations to the

publish

method
might occur before the

process

method is executed. For
performance purposes all these invocations are coalesced into one
invocation with concatenated arguments.

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

For example:

```java
publish("1");
publish("2", "3");
publish("4", "5", "6");
```

might result in:

```java
process("1", "2", "3", "4", "5", "6")
```

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

publish("1");
publish("2", "3");
publish("4", "5", "6");

process("1", "2", "3", "4", "5", "6")

Sample Usage

. This code snippet loads some tabular data and
updates

DefaultTableModel

with it. Note that it safe to mutate
the tableModel from inside the

process

method because it is
invoked on the

Event Dispatch Thread

.

```java
class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}
```

class TableSwingWorker extends
SwingWorker<DefaultTableModel, Object[]> {
private final DefaultTableModel tableModel;

public TableSwingWorker(DefaultTableModel tableModel) {
this.tableModel = tableModel;
}

@Override

protected DefaultTableModel doInBackground() throws Exception {
for (Object[] row = loadData();
! isCancelled() && row != null;
row = loadData()) {
publish((Object[]) row);
}
return tableModel;
}

@Override

protected void process(List<Object[]> chunks) {
for (Object[] row : chunks) {
tableModel.addRow(row);
}
}
}

process

```java
protected void process​(
List
<
V
> chunks)
```

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Please refer to the

publish(V...)

method for more details.

**Parameters:** chunks

- intermediate results to process
**See Also:** publish(V...)

---

#### process

protected void process​(

List

<

V

> chunks)

Receives data chunks from the

publish

method asynchronously on the

Event Dispatch Thread

.

Please refer to the

publish(V...)

method for more details.

Please refer to the

publish(V...)

method for more details.

done

```java
protected void done()
```

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished. The default
implementation does nothing. Subclasses may override this method to
perform completion actions on the

Event Dispatch Thread

. Note
that you can query status inside the implementation of this method to
determine the result of this task or whether this task has been cancelled.

**See Also:** doInBackground()

,

Future.isCancelled()

,

get()

---

#### done

protected void done()

Executed on the

Event Dispatch Thread

after the

doInBackground

method is finished. The default
implementation does nothing. Subclasses may override this method to
perform completion actions on the

Event Dispatch Thread

. Note
that you can query status inside the implementation of this method to
determine the result of this task or whether this task has been cancelled.

setProgress

```java
protected final void setProgress​(int progress)
```

Sets the

progress

bound property.
The value should be from 0 to 100.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

**Parameters:** progress

- the progress value to set
**Throws:** IllegalArgumentException

- is value not from 0 to 100

---

#### setProgress

protected final void setProgress​(int progress)

Sets the

progress

bound property.
The value should be from 0 to 100.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

Because

PropertyChangeListener

s are notified asynchronously on
the

Event Dispatch Thread

multiple invocations to the

setProgress

method might occur before any

PropertyChangeListeners

are invoked. For performance purposes
all these invocations are coalesced into one invocation with the last
invocation argument only.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

For example, the following invokations:

```java
setProgress(1);
setProgress(2);
setProgress(3);
```

might result in a single

PropertyChangeListener

notification with
the value

3

.

setProgress(1);
setProgress(2);
setProgress(3);

getProgress

```java
public final int getProgress()
```

Returns the

progress

bound property.

**Returns:** the progress bound property.

---

#### getProgress

public final int getProgress()

Returns the

progress

bound property.

execute

```java
public final void execute()
```

Schedules this

SwingWorker

for execution on a

worker

thread. There are a number of

worker

threads available. In the
event all

worker

threads are busy handling other

SwingWorkers

this

SwingWorker

is placed in a waiting
queue.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

---

#### execute

public final void execute()

Schedules this

SwingWorker

for execution on a

worker

thread. There are a number of

worker

threads available. In the
event all

worker

threads are busy handling other

SwingWorkers

this

SwingWorker

is placed in a waiting
queue.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

Note:

SwingWorker

is only designed to be executed once. Executing a

SwingWorker

more than once will not result in invoking the

doInBackground

method twice.

get

```java
public final
T
get()
throws
InterruptedException
,

ExecutionException
```

Waits if necessary for the computation to complete, and then
retrieves its result.

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

**Specified by:** get

in interface

Future

<

T

>
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception

---

#### get

public final

T

get()
throws

InterruptedException

,

ExecutionException

Waits if necessary for the computation to complete, and then
retrieves its result.

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

Note: calling

get

on the

Event Dispatch Thread

blocks

all

events, including repaints, from being processed until this

SwingWorker

is complete.

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

When you want the

SwingWorker

to block on the

Event
Dispatch Thread

we recommend that you use a

modal dialog

.

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

For example:

```java
class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);
```

class SwingWorkerCompletionWaiter implements PropertyChangeListener {
private JDialog dialog;

public SwingWorkerCompletionWaiter(JDialog dialog) {
this.dialog = dialog;
}

public void propertyChange(PropertyChangeEvent event) {
if ("state".equals(event.getPropertyName())
&& SwingWorker.StateValue.DONE == event.getNewValue()) {
dialog.setVisible(false);
dialog.dispose();
}
}
}
JDialog dialog = new JDialog(owner, true);
swingWorker.addPropertyChangeListener(
new SwingWorkerCompletionWaiter(dialog));
swingWorker.execute();
//the dialog will be visible until the SwingWorker is done
dialog.setVisible(true);

get

```java
public final
T
get​(long timeout,

TimeUnit
unit)
throws
InterruptedException
,

ExecutionException
,

TimeoutException
```

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Please refer to

get()

for more details.

**Specified by:** get

in interface

Future

<

T

>
**Parameters:** timeout

- the maximum time to wait
**Parameters:** unit

- the time unit of the timeout argument
**Returns:** the computed result
**Throws:** CancellationException

- if the computation was cancelled
**Throws:** InterruptedException

- if the current thread was interrupted
while waiting
**Throws:** ExecutionException

- if the computation threw an
exception
**Throws:** TimeoutException

- if the wait timed out

---

#### get

public final

T

get​(long timeout,

TimeUnit

unit)
throws

InterruptedException

,

ExecutionException

,

TimeoutException

Waits if necessary for at most the given time for the computation
to complete, and then retrieves its result, if available.

Please refer to

get()

for more details.

Please refer to

get()

for more details.

addPropertyChangeListener

```java
public final void addPropertyChangeListener​(
PropertyChangeListener
listener)
```

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all properties. The same listener object may be added
more than once, and will be called as many times as it is added. If

listener

is

null

, no exception is thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be added

---

#### addPropertyChangeListener

public final void addPropertyChangeListener​(

PropertyChangeListener

listener)

Adds a

PropertyChangeListener

to the listener list. The listener
is registered for all properties. The same listener object may be added
more than once, and will be called as many times as it is added. If

listener

is

null

, no exception is thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

removePropertyChangeListener

```java
public final void removePropertyChangeListener​(
PropertyChangeListener
listener)
```

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** listener

- the

PropertyChangeListener

to be removed

---

#### removePropertyChangeListener

public final void removePropertyChangeListener​(

PropertyChangeListener

listener)

Removes a

PropertyChangeListener

from the listener list. This
removes a

PropertyChangeListener

that was registered for all
properties. If

listener

was added more than once to the same
event source, it will be notified one less time after being removed. If

listener

is

null

, or was never added, no exception is
thrown and no action is taken.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

firePropertyChange

```java
public final void firePropertyChange​(
String
propertyName,

Object
oldValue,

Object
newValue)
```

Reports a bound property update to any registered listeners. No event is
fired if

old

and

new

are equal and non-null.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

**Parameters:** propertyName

- the programmatic name of the property that was
changed
**Parameters:** oldValue

- the old value of the property
**Parameters:** newValue

- the new value of the property

---

#### firePropertyChange

public final void firePropertyChange​(

String

propertyName,

Object

oldValue,

Object

newValue)

Reports a bound property update to any registered listeners. No event is
fired if

old

and

new

are equal and non-null.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

This

SwingWorker

will be the source for
any generated events.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

When called off the

Event Dispatch Thread

PropertyChangeListeners

are notified asynchronously on
the

Event Dispatch Thread

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

Note: This is merely a convenience wrapper. All work is delegated to

PropertyChangeSupport

from

getPropertyChangeSupport()

.

getPropertyChangeSupport

```java
public final
PropertyChangeSupport
getPropertyChangeSupport()
```

Returns the

PropertyChangeSupport

for this

SwingWorker

.
This method is used when flexible access to bound properties support is
needed.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

**Returns:** PropertyChangeSupport

for this

SwingWorker

---

#### getPropertyChangeSupport

public final

PropertyChangeSupport

getPropertyChangeSupport()

Returns the

PropertyChangeSupport

for this

SwingWorker

.
This method is used when flexible access to bound properties support is
needed.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

This

SwingWorker

will be the source for
any generated events.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

Note: The returned

PropertyChangeSupport

notifies any

PropertyChangeListener

s asynchronously on the

Event Dispatch
Thread

in the event that

firePropertyChange

or

fireIndexedPropertyChange

are called off the

Event Dispatch
Thread

.

getState

```java
public final
SwingWorker.StateValue
getState()
```

Returns the

SwingWorker

state bound property.

**Returns:** the current state

---

#### getState

public final

SwingWorker.StateValue

getState()

Returns the

SwingWorker

state bound property.

---

