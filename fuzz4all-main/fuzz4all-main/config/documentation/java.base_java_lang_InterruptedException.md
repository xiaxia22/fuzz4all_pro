# Class InterruptedException

**Source:** `java.base\java\lang\InterruptedException.html`

### Class Description

```java
public class
InterruptedException

extends
Exception
```

Thrown when a thread is waiting, sleeping, or otherwise occupied,
and the thread is interrupted, either before or during the activity.
Occasionally a method may wish to test whether the current
thread has been interrupted, and if so, to immediately throw
this exception. The following code can be used to achieve
this effect:

```java
if (Thread.interrupted()) // Clears interrupted status!
throw new InterruptedException();
```

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public InterruptedException()

Constructs an

InterruptedException

with no detail message.

---

#### public InterruptedException​(
String
s)

Constructs an

InterruptedException

with the
specified detail message.

**Parameters:**
- s

- the detail message.

---

### Method Details

*No entries found.*

### Additional Sections

#### Class InterruptedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - java.lang.InterruptedException

java.lang.Throwable

- java.lang.Exception
- - java.lang.InterruptedException

java.lang.Exception

- java.lang.InterruptedException

java.lang.InterruptedException

**All Implemented Interfaces:** Serializable

```java
public class
InterruptedException

extends
Exception
```

Thrown when a thread is waiting, sleeping, or otherwise occupied,
and the thread is interrupted, either before or during the activity.
Occasionally a method may wish to test whether the current
thread has been interrupted, and if so, to immediately throw
this exception. The following code can be used to achieve
this effect:

```java
if (Thread.interrupted()) // Clears interrupted status!
throw new InterruptedException();
```

**Since:** 1.0
**See Also:** Object.wait()

,

Object.wait(long)

,

Object.wait(long, int)

,

Thread.sleep(long)

,

Thread.interrupt()

,

Thread.interrupted()

,

Serialized Form

public class

InterruptedException

extends

Exception

Thrown when a thread is waiting, sleeping, or otherwise occupied,
and the thread is interrupted, either before or during the activity.
Occasionally a method may wish to test whether the current
thread has been interrupted, and if so, to immediately throw
this exception. The following code can be used to achieve
this effect:

```java
if (Thread.interrupted()) // Clears interrupted status!
throw new InterruptedException();
```

if (Thread.interrupted()) // Clears interrupted status!
throw new InterruptedException();

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

InterruptedException

()

Constructs an

InterruptedException

with no detail message.

InterruptedException

​(

String

s)

Constructs an

InterruptedException

with the
specified detail message.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

InterruptedException

()

Constructs an

InterruptedException

with no detail message.

InterruptedException

​(

String

s)

Constructs an

InterruptedException

with the
specified detail message.

---

#### Constructor Summary

Constructs an

InterruptedException

with no detail message.

Constructs an

InterruptedException

with the
specified detail message.

Method Summary

- Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

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

Methods declared in class java.lang.

Throwable

addSuppressed

,

fillInStackTrace

,

getCause

,

getLocalizedMessage

,

getMessage

,

getStackTrace

,

getSuppressed

,

initCause

,

printStackTrace

,

printStackTrace

,

printStackTrace

,

setStackTrace

,

toString

---

#### Methods declared in class java.lang. Throwable

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

- InterruptedException

```java
public InterruptedException()
```

Constructs an

InterruptedException

with no detail message.

- InterruptedException

```java
public InterruptedException​(
String
s)
```

Constructs an

InterruptedException

with the
specified detail message.

**Parameters:** s

- the detail message.

Constructor Detail

- InterruptedException

```java
public InterruptedException()
```

Constructs an

InterruptedException

with no detail message.

- InterruptedException

```java
public InterruptedException​(
String
s)
```

Constructs an

InterruptedException

with the
specified detail message.

**Parameters:** s

- the detail message.

---

#### Constructor Detail

InterruptedException

```java
public InterruptedException()
```

Constructs an

InterruptedException

with no detail message.

---

#### InterruptedException

public InterruptedException()

Constructs an

InterruptedException

with no detail message.

InterruptedException

```java
public InterruptedException​(
String
s)
```

Constructs an

InterruptedException

with the
specified detail message.

**Parameters:** s

- the detail message.

---

#### InterruptedException

public InterruptedException​(

String

s)

Constructs an

InterruptedException

with the
specified detail message.

---

