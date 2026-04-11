# Interface RemoteCall

**Source:** `java.rmi\java\rmi\server\RemoteCall.html`

### Class Description

```java
@Deprecated

public interface
RemoteCall
```

RemoteCall

is an abstraction used solely by the RMI runtime
(in conjunction with stubs and skeletons of remote objects) to carry out a
call to a remote object. The

RemoteCall

interface is
deprecated because it is only used by deprecated methods of

java.rmi.server.RemoteRef

.

**Since:** 1.1
**See Also:** RemoteRef

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### @Deprecated

ObjectOutput
getOutputStream()
throws
IOException

Return the output stream the stub/skeleton should put arguments/results
into.

**Returns:**
- output stream for arguments/results

**Throws:**
- IOException

- if an I/O error occurs.

**Since:**
- 1.1

---

#### @Deprecated

void releaseOutputStream()
throws
IOException

Release the output stream; in some transports this would release
the stream.

**Throws:**
- IOException

- if an I/O error occurs.

**Since:**
- 1.1

---

#### @Deprecated

ObjectInput
getInputStream()
throws
IOException

Get the InputStream that the stub/skeleton should get
results/arguments from.

**Returns:**
- input stream for reading arguments/results

**Throws:**
- IOException

- if an I/O error occurs.

**Since:**
- 1.1

---

#### @Deprecated

void releaseInputStream()
throws
IOException

Release the input stream. This would allow some transports to release
the channel early.

**Throws:**
- IOException

- if an I/O error occurs.

**Since:**
- 1.1

---

#### @Deprecated

ObjectOutput
getResultStream​(boolean success)
throws
IOException
,

StreamCorruptedException

Returns an output stream (may put out header information
relating to the success of the call). Should only succeed
once per remote call.

**Parameters:**
- success

- If true, indicates normal return, else indicates
exceptional return.

**Returns:**
- output stream for writing call result

**Throws:**
- IOException

- if an I/O error occurs.
- StreamCorruptedException

- If already been called.

**Since:**
- 1.1

---

#### @Deprecated

void executeCall()
throws
Exception

Do whatever it takes to execute the call.

**Throws:**
- Exception

- if a general exception occurs.

**Since:**
- 1.1

---

#### @Deprecated

void done()
throws
IOException

Allow cleanup after the remote call has completed.

**Throws:**
- IOException

- if an I/O error occurs.

**Since:**
- 1.1

---

### Additional Sections

#### Interface RemoteCall

```java
@Deprecated

public interface
RemoteCall
```

Deprecated.

no replacement.

RemoteCall

is an abstraction used solely by the RMI runtime
(in conjunction with stubs and skeletons of remote objects) to carry out a
call to a remote object. The

RemoteCall

interface is
deprecated because it is only used by deprecated methods of

java.rmi.server.RemoteRef

.

**Since:** 1.1
**See Also:** RemoteRef

@Deprecated

public interface

RemoteCall

RemoteCall

is an abstraction used solely by the RMI runtime
(in conjunction with stubs and skeletons of remote objects) to carry out a
call to a remote object. The

RemoteCall

interface is
deprecated because it is only used by deprecated methods of

java.rmi.server.RemoteRef

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

done

()

Deprecated.

no replacement

void

executeCall

()

Deprecated.

no replacement

ObjectInput

getInputStream

()

Deprecated.

no replacement

ObjectOutput

getOutputStream

()

Deprecated.

no replacement

ObjectOutput

getResultStream

​(boolean success)

Deprecated.

no replacement

void

releaseInputStream

()

Deprecated.

no replacement

void

releaseOutputStream

()

Deprecated.

no replacement

Method Summary

All Methods

Instance Methods

Abstract Methods

Deprecated Methods

Modifier and Type

Method

Description

void

done

()

Deprecated.

no replacement

void

executeCall

()

Deprecated.

no replacement

ObjectInput

getInputStream

()

Deprecated.

no replacement

ObjectOutput

getOutputStream

()

Deprecated.

no replacement

ObjectOutput

getResultStream

​(boolean success)

Deprecated.

no replacement

void

releaseInputStream

()

Deprecated.

no replacement

void

releaseOutputStream

()

Deprecated.

no replacement

---

#### Method Summary

Deprecated.

no replacement

============ METHOD DETAIL ==========

- Method Detail

- getOutputStream

```java
@Deprecated

ObjectOutput
getOutputStream()
throws
IOException
```

Deprecated.

no replacement

Return the output stream the stub/skeleton should put arguments/results
into.

**Returns:** output stream for arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- releaseOutputStream

```java
@Deprecated

void releaseOutputStream()
throws
IOException
```

Deprecated.

no replacement

Release the output stream; in some transports this would release
the stream.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- getInputStream

```java
@Deprecated

ObjectInput
getInputStream()
throws
IOException
```

Deprecated.

no replacement

Get the InputStream that the stub/skeleton should get
results/arguments from.

**Returns:** input stream for reading arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- releaseInputStream

```java
@Deprecated

void releaseInputStream()
throws
IOException
```

Deprecated.

no replacement

Release the input stream. This would allow some transports to release
the channel early.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- getResultStream

```java
@Deprecated

ObjectOutput
getResultStream​(boolean success)
throws
IOException
,

StreamCorruptedException
```

Deprecated.

no replacement

Returns an output stream (may put out header information
relating to the success of the call). Should only succeed
once per remote call.

**Parameters:** success

- If true, indicates normal return, else indicates
exceptional return.
**Returns:** output stream for writing call result
**Throws:** IOException

- if an I/O error occurs.
**Throws:** StreamCorruptedException

- If already been called.
**Since:** 1.1

- executeCall

```java
@Deprecated

void executeCall()
throws
Exception
```

Deprecated.

no replacement

Do whatever it takes to execute the call.

**Throws:** Exception

- if a general exception occurs.
**Since:** 1.1

- done

```java
@Deprecated

void done()
throws
IOException
```

Deprecated.

no replacement

Allow cleanup after the remote call has completed.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

Method Detail

- getOutputStream

```java
@Deprecated

ObjectOutput
getOutputStream()
throws
IOException
```

Deprecated.

no replacement

Return the output stream the stub/skeleton should put arguments/results
into.

**Returns:** output stream for arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- releaseOutputStream

```java
@Deprecated

void releaseOutputStream()
throws
IOException
```

Deprecated.

no replacement

Release the output stream; in some transports this would release
the stream.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- getInputStream

```java
@Deprecated

ObjectInput
getInputStream()
throws
IOException
```

Deprecated.

no replacement

Get the InputStream that the stub/skeleton should get
results/arguments from.

**Returns:** input stream for reading arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- releaseInputStream

```java
@Deprecated

void releaseInputStream()
throws
IOException
```

Deprecated.

no replacement

Release the input stream. This would allow some transports to release
the channel early.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

- getResultStream

```java
@Deprecated

ObjectOutput
getResultStream​(boolean success)
throws
IOException
,

StreamCorruptedException
```

Deprecated.

no replacement

Returns an output stream (may put out header information
relating to the success of the call). Should only succeed
once per remote call.

**Parameters:** success

- If true, indicates normal return, else indicates
exceptional return.
**Returns:** output stream for writing call result
**Throws:** IOException

- if an I/O error occurs.
**Throws:** StreamCorruptedException

- If already been called.
**Since:** 1.1

- executeCall

```java
@Deprecated

void executeCall()
throws
Exception
```

Deprecated.

no replacement

Do whatever it takes to execute the call.

**Throws:** Exception

- if a general exception occurs.
**Since:** 1.1

- done

```java
@Deprecated

void done()
throws
IOException
```

Deprecated.

no replacement

Allow cleanup after the remote call has completed.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### Method Detail

getOutputStream

```java
@Deprecated

ObjectOutput
getOutputStream()
throws
IOException
```

Deprecated.

no replacement

Return the output stream the stub/skeleton should put arguments/results
into.

**Returns:** output stream for arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### getOutputStream

@Deprecated

ObjectOutput

getOutputStream()
throws

IOException

Return the output stream the stub/skeleton should put arguments/results
into.

releaseOutputStream

```java
@Deprecated

void releaseOutputStream()
throws
IOException
```

Deprecated.

no replacement

Release the output stream; in some transports this would release
the stream.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### releaseOutputStream

@Deprecated

void releaseOutputStream()
throws

IOException

Release the output stream; in some transports this would release
the stream.

getInputStream

```java
@Deprecated

ObjectInput
getInputStream()
throws
IOException
```

Deprecated.

no replacement

Get the InputStream that the stub/skeleton should get
results/arguments from.

**Returns:** input stream for reading arguments/results
**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### getInputStream

@Deprecated

ObjectInput

getInputStream()
throws

IOException

Get the InputStream that the stub/skeleton should get
results/arguments from.

releaseInputStream

```java
@Deprecated

void releaseInputStream()
throws
IOException
```

Deprecated.

no replacement

Release the input stream. This would allow some transports to release
the channel early.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### releaseInputStream

@Deprecated

void releaseInputStream()
throws

IOException

Release the input stream. This would allow some transports to release
the channel early.

getResultStream

```java
@Deprecated

ObjectOutput
getResultStream​(boolean success)
throws
IOException
,

StreamCorruptedException
```

Deprecated.

no replacement

Returns an output stream (may put out header information
relating to the success of the call). Should only succeed
once per remote call.

**Parameters:** success

- If true, indicates normal return, else indicates
exceptional return.
**Returns:** output stream for writing call result
**Throws:** IOException

- if an I/O error occurs.
**Throws:** StreamCorruptedException

- If already been called.
**Since:** 1.1

---

#### getResultStream

@Deprecated

ObjectOutput

getResultStream​(boolean success)
throws

IOException

,

StreamCorruptedException

Returns an output stream (may put out header information
relating to the success of the call). Should only succeed
once per remote call.

executeCall

```java
@Deprecated

void executeCall()
throws
Exception
```

Deprecated.

no replacement

Do whatever it takes to execute the call.

**Throws:** Exception

- if a general exception occurs.
**Since:** 1.1

---

#### executeCall

@Deprecated

void executeCall()
throws

Exception

Do whatever it takes to execute the call.

done

```java
@Deprecated

void done()
throws
IOException
```

Deprecated.

no replacement

Allow cleanup after the remote call has completed.

**Throws:** IOException

- if an I/O error occurs.
**Since:** 1.1

---

#### done

@Deprecated

void done()
throws

IOException

Allow cleanup after the remote call has completed.

---

