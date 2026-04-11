# Class ProgressMonitorInputStream

**Source:** `java.desktop\javax\swing\ProgressMonitorInputStream.html`

### Class Description

```java
public class
ProgressMonitorInputStream

extends
FilterInputStream
```

Monitors the progress of reading from some InputStream. This ProgressMonitor
is normally invoked in roughly this form:

```java
InputStream in = new BufferedInputStream(
new ProgressMonitorInputStream(
parentComponent,
"Reading " + fileName,
new FileInputStream(fileName)));
```

This creates a progress monitor to monitor the progress of reading
the input stream. If it's taking a while, a ProgressDialog will
be popped up to inform the user. If the user hits the Cancel button
an InterruptedIOException will be thrown on the next read.
All the right cleanup is done when the stream is closed.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

**All Implemented Interfaces:** Closeable

,

AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ProgressMonitorInputStream​(
Component
parentComponent,

Object
message,

InputStream
in)

Constructs an object to monitor the progress of an input stream.

**Parameters:**
- message

- Descriptive text to be placed in the dialog box
if one is popped up.
- parentComponent

- The component triggering the operation
being monitored.
- in

- The input stream to be monitored.

---

### Method Details

#### public
ProgressMonitor
getProgressMonitor()

Get the ProgressMonitor object being used by this stream. Normally
this isn't needed unless you want to do something like change the
descriptive text partway through reading the file.

**Returns:**
- the ProgressMonitor object used by this object

---

#### public int read()
throws
IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:**
- read

in class

FilterInputStream

**Returns:**
- the next byte of data, or

-1

if the end of the
stream is reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.in

---

#### public int read​(byte[] b)
throws
IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the buffer into which the data is read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.read(byte[], int, int)

---

#### public int read​(byte[] b,
int off,
int len)
throws
IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:**
- read

in class

FilterInputStream

**Parameters:**
- b

- the buffer into which the data is read.
- off

- the start offset in the destination array

b
- len

- the maximum number of bytes read.

**Returns:**
- the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.in

---

#### public long skip​(long n)
throws
IOException

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

**Overrides:**
- skip

in class

FilterInputStream

**Parameters:**
- n

- the number of bytes to be skipped.

**Returns:**
- the actual number of bytes skipped.

**Throws:**
- IOException

- if

in.skip(n)

throws an IOException.

---

#### public void close()
throws
IOException

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

**Specified by:**
- close

in interface

AutoCloseable
- close

in interface

Closeable

**Overrides:**
- close

in class

FilterInputStream

**Throws:**
- IOException

- if an I/O error occurs.

**See Also:**
- FilterInputStream.in

---

#### public void reset()
throws
IOException

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

**Overrides:**
- reset

in class

FilterInputStream

**Throws:**
- IOException

- if the stream has not been marked or if the
mark has been invalidated.

**See Also:**
- FilterInputStream.in

,

FilterInputStream.mark(int)

---

### Additional Sections

#### Class ProgressMonitorInputStream

java.lang.Object

- java.io.InputStream
- - java.io.FilterInputStream
- - javax.swing.ProgressMonitorInputStream

java.io.InputStream

- java.io.FilterInputStream
- - javax.swing.ProgressMonitorInputStream

java.io.FilterInputStream

- javax.swing.ProgressMonitorInputStream

javax.swing.ProgressMonitorInputStream

**All Implemented Interfaces:** Closeable

,

AutoCloseable

```java
public class
ProgressMonitorInputStream

extends
FilterInputStream
```

Monitors the progress of reading from some InputStream. This ProgressMonitor
is normally invoked in roughly this form:

```java
InputStream in = new BufferedInputStream(
new ProgressMonitorInputStream(
parentComponent,
"Reading " + fileName,
new FileInputStream(fileName)));
```

This creates a progress monitor to monitor the progress of reading
the input stream. If it's taking a while, a ProgressDialog will
be popped up to inform the user. If the user hits the Cancel button
an InterruptedIOException will be thrown on the next read.
All the right cleanup is done when the stream is closed.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

**Since:** 1.2
**See Also:** ProgressMonitor

,

JOptionPane

public class

ProgressMonitorInputStream

extends

FilterInputStream

Monitors the progress of reading from some InputStream. This ProgressMonitor
is normally invoked in roughly this form:

```java
InputStream in = new BufferedInputStream(
new ProgressMonitorInputStream(
parentComponent,
"Reading " + fileName,
new FileInputStream(fileName)));
```

This creates a progress monitor to monitor the progress of reading
the input stream. If it's taking a while, a ProgressDialog will
be popped up to inform the user. If the user hits the Cancel button
an InterruptedIOException will be thrown on the next read.
All the right cleanup is done when the stream is closed.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

InputStream in = new BufferedInputStream(
new ProgressMonitorInputStream(
parentComponent,
"Reading " + fileName,
new FileInputStream(fileName)));

This creates a progress monitor to monitor the progress of reading
the input stream. If it's taking a while, a ProgressDialog will
be popped up to inform the user. If the user hits the Cancel button
an InterruptedIOException will be thrown on the next read.
All the right cleanup is done when the stream is closed.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

For further documentation and examples see

How to Monitor Progress

,
a section in

The Java Tutorial.

=========== FIELD SUMMARY ===========

- Field Summary

- Fields declared in class java.io.

FilterInputStream

in

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ProgressMonitorInputStream

​(

Component

parentComponent,

Object

message,

InputStream

in)

Constructs an object to monitor the progress of an input stream.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

ProgressMonitor

getProgressMonitor

()

Get the ProgressMonitor object being used by this stream.

int

read

()

Overrides

FilterInputStream.read

to update the progress monitor after the read.

int

read

​(byte[] b)

Overrides

FilterInputStream.read

to update the progress monitor after the read.

int

read

​(byte[] b,
int off,
int len)

Overrides

FilterInputStream.read

to update the progress monitor after the read.

void

reset

()

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

long

skip

​(long n)

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

- Methods declared in class java.io.

FilterInputStream

available

,

mark

,

markSupported

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

Field Summary

- Fields declared in class java.io.

FilterInputStream

in

---

#### Field Summary

Fields declared in class java.io.

FilterInputStream

in

---

#### Fields declared in class java.io. FilterInputStream

Constructor Summary

Constructors

Constructor

Description

ProgressMonitorInputStream

​(

Component

parentComponent,

Object

message,

InputStream

in)

Constructs an object to monitor the progress of an input stream.

---

#### Constructor Summary

Constructs an object to monitor the progress of an input stream.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

close

()

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

ProgressMonitor

getProgressMonitor

()

Get the ProgressMonitor object being used by this stream.

int

read

()

Overrides

FilterInputStream.read

to update the progress monitor after the read.

int

read

​(byte[] b)

Overrides

FilterInputStream.read

to update the progress monitor after the read.

int

read

​(byte[] b,
int off,
int len)

Overrides

FilterInputStream.read

to update the progress monitor after the read.

void

reset

()

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

long

skip

​(long n)

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

- Methods declared in class java.io.

FilterInputStream

available

,

mark

,

markSupported

- Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

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

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

Get the ProgressMonitor object being used by this stream.

Overrides

FilterInputStream.read

to update the progress monitor after the read.

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

Methods declared in class java.io.

FilterInputStream

available

,

mark

,

markSupported

---

#### Methods declared in class java.io. FilterInputStream

Methods declared in class java.io.

InputStream

nullInputStream

,

readAllBytes

,

readNBytes

,

readNBytes

,

transferTo

---

#### Methods declared in class java.io. InputStream

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

- ProgressMonitorInputStream

```java
public ProgressMonitorInputStream​(
Component
parentComponent,

Object
message,

InputStream
in)
```

Constructs an object to monitor the progress of an input stream.

**Parameters:** message

- Descriptive text to be placed in the dialog box
if one is popped up.
**Parameters:** parentComponent

- The component triggering the operation
being monitored.
**Parameters:** in

- The input stream to be monitored.

============ METHOD DETAIL ==========

- Method Detail

- getProgressMonitor

```java
public
ProgressMonitor
getProgressMonitor()
```

Get the ProgressMonitor object being used by this stream. Normally
this isn't needed unless you want to do something like change the
descriptive text partway through reading the file.

**Returns:** the ProgressMonitor object used by this object

- read

```java
public int read()
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.read(byte[], int, int)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if

in.skip(n)

throws an IOException.

- close

```java
public void close()
throws
IOException
```

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- reset

```java
public void reset()
throws
IOException
```

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if the stream has not been marked or if the
mark has been invalidated.
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

Constructor Detail

- ProgressMonitorInputStream

```java
public ProgressMonitorInputStream​(
Component
parentComponent,

Object
message,

InputStream
in)
```

Constructs an object to monitor the progress of an input stream.

**Parameters:** message

- Descriptive text to be placed in the dialog box
if one is popped up.
**Parameters:** parentComponent

- The component triggering the operation
being monitored.
**Parameters:** in

- The input stream to be monitored.

---

#### Constructor Detail

ProgressMonitorInputStream

```java
public ProgressMonitorInputStream​(
Component
parentComponent,

Object
message,

InputStream
in)
```

Constructs an object to monitor the progress of an input stream.

**Parameters:** message

- Descriptive text to be placed in the dialog box
if one is popped up.
**Parameters:** parentComponent

- The component triggering the operation
being monitored.
**Parameters:** in

- The input stream to be monitored.

---

#### ProgressMonitorInputStream

public ProgressMonitorInputStream​(

Component

parentComponent,

Object

message,

InputStream

in)

Constructs an object to monitor the progress of an input stream.

Method Detail

- getProgressMonitor

```java
public
ProgressMonitor
getProgressMonitor()
```

Get the ProgressMonitor object being used by this stream. Normally
this isn't needed unless you want to do something like change the
descriptive text partway through reading the file.

**Returns:** the ProgressMonitor object used by this object

- read

```java
public int read()
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- read

```java
public int read​(byte[] b)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.read(byte[], int, int)

- read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- skip

```java
public long skip​(long n)
throws
IOException
```

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if

in.skip(n)

throws an IOException.

- close

```java
public void close()
throws
IOException
```

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

- reset

```java
public void reset()
throws
IOException
```

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if the stream has not been marked or if the
mark has been invalidated.
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

---

#### Method Detail

getProgressMonitor

```java
public
ProgressMonitor
getProgressMonitor()
```

Get the ProgressMonitor object being used by this stream. Normally
this isn't needed unless you want to do something like change the
descriptive text partway through reading the file.

**Returns:** the ProgressMonitor object used by this object

---

#### getProgressMonitor

public

ProgressMonitor

getProgressMonitor()

Get the ProgressMonitor object being used by this stream. Normally
this isn't needed unless you want to do something like change the
descriptive text partway through reading the file.

read

```java
public int read()
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Returns:** the next byte of data, or

-1

if the end of the
stream is reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

---

#### read

public int read()
throws

IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

read

```java
public int read​(byte[] b)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.read(byte[], int, int)

---

#### read

public int read​(byte[] b)
throws

IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

read

```java
public int read​(byte[] b,
int off,
int len)
throws
IOException
```

Overrides

FilterInputStream.read

to update the progress monitor after the read.

**Overrides:** read

in class

FilterInputStream
**Parameters:** b

- the buffer into which the data is read.
**Parameters:** off

- the start offset in the destination array

b
**Parameters:** len

- the maximum number of bytes read.
**Returns:** the total number of bytes read into the buffer, or

-1

if there is no more data because the end of
the stream has been reached.
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

---

#### read

public int read​(byte[] b,
int off,
int len)
throws

IOException

Overrides

FilterInputStream.read

to update the progress monitor after the read.

skip

```java
public long skip​(long n)
throws
IOException
```

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

**Overrides:** skip

in class

FilterInputStream
**Parameters:** n

- the number of bytes to be skipped.
**Returns:** the actual number of bytes skipped.
**Throws:** IOException

- if

in.skip(n)

throws an IOException.

---

#### skip

public long skip​(long n)
throws

IOException

Overrides

FilterInputStream.skip

to update the progress monitor after the skip.

close

```java
public void close()
throws
IOException
```

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

**Specified by:** close

in interface

AutoCloseable
**Specified by:** close

in interface

Closeable
**Overrides:** close

in class

FilterInputStream
**Throws:** IOException

- if an I/O error occurs.
**See Also:** FilterInputStream.in

---

#### close

public void close()
throws

IOException

Overrides

FilterInputStream.close

to close the progress monitor as well as the stream.

reset

```java
public void reset()
throws
IOException
```

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

**Overrides:** reset

in class

FilterInputStream
**Throws:** IOException

- if the stream has not been marked or if the
mark has been invalidated.
**See Also:** FilterInputStream.in

,

FilterInputStream.mark(int)

---

#### reset

public void reset()
throws

IOException

Overrides

FilterInputStream.reset

to reset the progress monitor as well as the stream.

---

