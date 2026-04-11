# Interface ByteChannel

**Source:** `java.base\java\nio\channels\ByteChannel.html`

### Class Description

```java
public interface
ByteChannel

extends
ReadableByteChannel
,
WritableByteChannel
```

A channel that can read and write bytes. This interface simply unifies

ReadableByteChannel

and

WritableByteChannel

; it does not
specify any new operations.

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

ReadableByteChannel

,

WritableByteChannel

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

*No entries found.*

### Additional Sections

#### Interface ByteChannel

**All Superinterfaces:** AutoCloseable

,

Channel

,

Closeable

,

ReadableByteChannel

,

WritableByteChannel

**All Known Subinterfaces:** SeekableByteChannel

**All Known Implementing Classes:** DatagramChannel

,

FileChannel

,

SocketChannel

```java
public interface
ByteChannel

extends
ReadableByteChannel
,
WritableByteChannel
```

A channel that can read and write bytes. This interface simply unifies

ReadableByteChannel

and

WritableByteChannel

; it does not
specify any new operations.

**Since:** 1.4

public interface

ByteChannel

extends

ReadableByteChannel

,

WritableByteChannel

A channel that can read and write bytes. This interface simply unifies

ReadableByteChannel

and

WritableByteChannel

; it does not
specify any new operations.

========== METHOD SUMMARY ===========

- Method Summary

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

ReadableByteChannel

read

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

Method Summary

- Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

- Methods declared in interface java.nio.channels.

ReadableByteChannel

read

- Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

#### Method Summary

Methods declared in interface java.nio.channels.

Channel

close

,

isOpen

---

#### Methods declared in interface java.nio.channels. Channel

Methods declared in interface java.nio.channels.

ReadableByteChannel

read

---

#### Methods declared in interface java.nio.channels. ReadableByteChannel

Methods declared in interface java.nio.channels.

WritableByteChannel

write

---

