# Class LayoutQueue

**Source:** `java.desktop\javax\swing\text\LayoutQueue.html`

### Class Description

```java
public class
LayoutQueue

extends
Object
```

A queue of text layout tasks.

**Since:** 1.3
**See Also:** AsyncBoxView

---

### Field Details

*No entries found.*

### Constructor Details

#### public LayoutQueue()

Construct a layout queue.

---

### Method Details

#### public static
LayoutQueue
getDefaultQueue()

Fetch the default layout queue.

**Returns:**
- the default layout queue

---

#### public static void setDefaultQueue​(
LayoutQueue
q)

Set the default layout queue.

**Parameters:**
- q

- the new queue.

---

#### public void addTask​(
Runnable
task)

Add a task that is not needed immediately because
the results are not believed to be visible.

**Parameters:**
- task

- the task to add to the queue

---

#### protected
Runnable
waitForWork()

Used by the worker thread to get a new task to execute.

**Returns:**
- a task from the queue

---

### Additional Sections

#### Class LayoutQueue

java.lang.Object

- javax.swing.text.LayoutQueue

javax.swing.text.LayoutQueue

```java
public class
LayoutQueue

extends
Object
```

A queue of text layout tasks.

**Since:** 1.3
**See Also:** AsyncBoxView

public class

LayoutQueue

extends

Object

A queue of text layout tasks.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

LayoutQueue

()

Construct a layout queue.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTask

​(

Runnable

task)

Add a task that is not needed immediately because
the results are not believed to be visible.

static

LayoutQueue

getDefaultQueue

()

Fetch the default layout queue.

static void

setDefaultQueue

​(

LayoutQueue

q)

Set the default layout queue.

protected

Runnable

waitForWork

()

Used by the worker thread to get a new task to execute.

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

Constructor Summary

Constructors

Constructor

Description

LayoutQueue

()

Construct a layout queue.

---

#### Constructor Summary

Construct a layout queue.

Method Summary

All Methods

Static Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

addTask

​(

Runnable

task)

Add a task that is not needed immediately because
the results are not believed to be visible.

static

LayoutQueue

getDefaultQueue

()

Fetch the default layout queue.

static void

setDefaultQueue

​(

LayoutQueue

q)

Set the default layout queue.

protected

Runnable

waitForWork

()

Used by the worker thread to get a new task to execute.

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

---

#### Method Summary

Add a task that is not needed immediately because
the results are not believed to be visible.

Fetch the default layout queue.

Set the default layout queue.

Used by the worker thread to get a new task to execute.

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

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- LayoutQueue

```java
public LayoutQueue()
```

Construct a layout queue.

============ METHOD DETAIL ==========

- Method Detail

- getDefaultQueue

```java
public static
LayoutQueue
getDefaultQueue()
```

Fetch the default layout queue.

**Returns:** the default layout queue

- setDefaultQueue

```java
public static void setDefaultQueue​(
LayoutQueue
q)
```

Set the default layout queue.

**Parameters:** q

- the new queue.

- addTask

```java
public void addTask​(
Runnable
task)
```

Add a task that is not needed immediately because
the results are not believed to be visible.

**Parameters:** task

- the task to add to the queue

- waitForWork

```java
protected
Runnable
waitForWork()
```

Used by the worker thread to get a new task to execute.

**Returns:** a task from the queue

Constructor Detail

- LayoutQueue

```java
public LayoutQueue()
```

Construct a layout queue.

---

#### Constructor Detail

LayoutQueue

```java
public LayoutQueue()
```

Construct a layout queue.

---

#### LayoutQueue

public LayoutQueue()

Construct a layout queue.

Method Detail

- getDefaultQueue

```java
public static
LayoutQueue
getDefaultQueue()
```

Fetch the default layout queue.

**Returns:** the default layout queue

- setDefaultQueue

```java
public static void setDefaultQueue​(
LayoutQueue
q)
```

Set the default layout queue.

**Parameters:** q

- the new queue.

- addTask

```java
public void addTask​(
Runnable
task)
```

Add a task that is not needed immediately because
the results are not believed to be visible.

**Parameters:** task

- the task to add to the queue

- waitForWork

```java
protected
Runnable
waitForWork()
```

Used by the worker thread to get a new task to execute.

**Returns:** a task from the queue

---

#### Method Detail

getDefaultQueue

```java
public static
LayoutQueue
getDefaultQueue()
```

Fetch the default layout queue.

**Returns:** the default layout queue

---

#### getDefaultQueue

public static

LayoutQueue

getDefaultQueue()

Fetch the default layout queue.

setDefaultQueue

```java
public static void setDefaultQueue​(
LayoutQueue
q)
```

Set the default layout queue.

**Parameters:** q

- the new queue.

---

#### setDefaultQueue

public static void setDefaultQueue​(

LayoutQueue

q)

Set the default layout queue.

addTask

```java
public void addTask​(
Runnable
task)
```

Add a task that is not needed immediately because
the results are not believed to be visible.

**Parameters:** task

- the task to add to the queue

---

#### addTask

public void addTask​(

Runnable

task)

Add a task that is not needed immediately because
the results are not believed to be visible.

waitForWork

```java
protected
Runnable
waitForWork()
```

Used by the worker thread to get a new task to execute.

**Returns:** a task from the queue

---

#### waitForWork

protected

Runnable

waitForWork()

Used by the worker thread to get a new task to execute.

---

