# Interface Closeable

**Source:** `java.base\java\io\Closeable.html`

### Class Description

```java
public interface
Closeable

extends
AutoCloseable
```

A

Closeable

is a source or destination of data that can be closed.
The close method is invoked to release resources that the object is
holding (such as open files).

**All Superinterfaces:** AutoCloseable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void close()
throws
IOException

Closes this stream and releases any system resources associated
with it. If the stream is already closed then invoking this
method has no effect.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

**Specified by:**
- close

in interface

AutoCloseable

**Throws:**
- IOException

- if an I/O error occurs

---

### Additional Sections

#### Interface Closeable

**All Superinterfaces:** AutoCloseable

**All Known Subinterfaces:** AsynchronousByteChannel

,

AsynchronousChannel

,

ByteChannel

,

Channel

,

DirectoryStream

<T>

,

GatheringByteChannel

,

ImageInputStream

,

ImageOutputStream

,

InterruptibleChannel

,

JavaFileManager

,

JMXConnector

,

ModuleReader

,

MulticastChannel

,

NetworkChannel

,

ReadableByteChannel

,

RMIConnection

,

ScatteringByteChannel

,

SecureDirectoryStream

<T>

,

SeekableByteChannel

,

StandardJavaFileManager

,

WatchService

,

WritableByteChannel

**All Known Implementing Classes:** AbstractInterruptibleChannel

,

AbstractSelectableChannel

,

AbstractSelector

,

AsynchronousFileChannel

,

AsynchronousServerSocketChannel

,

AsynchronousSocketChannel

,

AudioInputStream

,

BufferedInputStream

,

BufferedOutputStream

,

BufferedReader

,

BufferedWriter

,

ByteArrayInputStream

,

ByteArrayOutputStream

,

CharArrayReader

,

CharArrayWriter

,

CheckedInputStream

,

CheckedOutputStream

,

CipherInputStream

,

CipherOutputStream

,

DatagramChannel

,

DatagramSocket

,

DataInputStream

,

DataOutputStream

,

DeflaterInputStream

,

DeflaterOutputStream

,

DigestInputStream

,

DigestOutputStream

,

FileCacheImageInputStream

,

FileCacheImageOutputStream

,

FileChannel

,

FileImageInputStream

,

FileImageOutputStream

,

FileInputStream

,

FileOutputStream

,

FileReader

,

FileSystem

,

FileWriter

,

FilterInputStream

,

FilterOutputStream

,

FilterReader

,

FilterWriter

,

Formatter

,

ForwardingJavaFileManager

,

GZIPInputStream

,

GZIPOutputStream

,

ImageInputStreamImpl

,

ImageOutputStreamImpl

,

InflaterInputStream

,

InflaterOutputStream

,

InputStream

,

InputStreamReader

,

JarFile

,

JarInputStream

,

JarOutputStream

,

LineNumberInputStream

,

LineNumberReader

,

LogStream

,

MemoryCacheImageInputStream

,

MemoryCacheImageOutputStream

,

MLet

,

MulticastSocket

,

ObjectInputStream

,

ObjectOutputStream

,

OutputStream

,

OutputStreamWriter

,

Pipe.SinkChannel

,

Pipe.SourceChannel

,

PipedInputStream

,

PipedOutputStream

,

PipedReader

,

PipedWriter

,

PrintStream

,

PrintWriter

,

PrivateMLet

,

ProgressMonitorInputStream

,

PushbackInputStream

,

PushbackReader

,

RandomAccessFile

,

Reader

,

Recording

,

RecordingFile

,

RMIConnectionImpl

,

RMIConnectionImpl_Stub

,

RMIConnector

,

RMIIIOPServerImpl

,

RMIJRMPServerImpl

,

RMIServerImpl

,

Scanner

,

SctpChannel

,

SctpMultiChannel

,

SctpServerChannel

,

SelectableChannel

,

Selector

,

SequenceInputStream

,

ServerSocket

,

ServerSocketChannel

,

Socket

,

SocketChannel

,

SSLServerSocket

,

SSLSocket

,

StringBufferInputStream

,

StringReader

,

StringWriter

,

URLClassLoader

,

URLReader

,

Writer

,

ZipFile

,

ZipInputStream

,

ZipOutputStream

```java
public interface
Closeable

extends
AutoCloseable
```

A

Closeable

is a source or destination of data that can be closed.
The close method is invoked to release resources that the object is
holding (such as open files).

**Since:** 1.5

public interface

Closeable

extends

AutoCloseable

A

Closeable

is a source or destination of data that can be closed.
The close method is invoked to release resources that the object is
holding (such as open files).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this stream and releases any system resources associated
with it.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

close

()

Closes this stream and releases any system resources associated
with it.

---

#### Method Summary

Closes this stream and releases any system resources associated
with it.

============ METHOD DETAIL ==========

- Method Detail

- close

```java
void close()
throws
IOException
```

Closes this stream and releases any system resources associated
with it. If the stream is already closed then invoking this
method has no effect.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- if an I/O error occurs

Method Detail

- close

```java
void close()
throws
IOException
```

Closes this stream and releases any system resources associated
with it. If the stream is already closed then invoking this
method has no effect.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- if an I/O error occurs

---

#### Method Detail

close

```java
void close()
throws
IOException
```

Closes this stream and releases any system resources associated
with it. If the stream is already closed then invoking this
method has no effect.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

**Specified by:** close

in interface

AutoCloseable
**Throws:** IOException

- if an I/O error occurs

---

#### close

void close()
throws

IOException

Closes this stream and releases any system resources associated
with it. If the stream is already closed then invoking this
method has no effect.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

As noted in

AutoCloseable.close()

, cases where the
close may fail require careful attention. It is strongly advised
to relinquish the underlying resources and to internally

mark

the

Closeable

as closed, prior to throwing
the

IOException

.

---

