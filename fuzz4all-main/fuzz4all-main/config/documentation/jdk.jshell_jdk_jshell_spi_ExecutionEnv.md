# Interface ExecutionEnv

**Source:** `jdk.jshell\jdk\jshell\spi\ExecutionEnv.html`

### Class Description

```java
public interface
ExecutionEnv
```

Functionality made available to a pluggable JShell execution engine. It is
provided to the execution engine by the core JShell implementation.

This interface is designed to provide the access to core JShell functionality
needed to implement ExecutionControl.

**Since:** 9
**See Also:** ExecutionControl

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### InputStream
userIn()

Returns the user's input stream.

**Returns:**
- the user's input stream

---

#### PrintStream
userOut()

Returns the user's output stream.

**Returns:**
- the user's output stream

---

#### PrintStream
userErr()

Returns the user's error stream.

**Returns:**
- the user's error stream

---

#### List
<
String
> extraRemoteVMOptions()

Returns the additional VM options to be used when launching the remote
JVM. This is advice to the execution engine.

Note: an execution engine need not launch a remote JVM.

**Returns:**
- the additional options with which to launch the remote JVM

---

#### void closeDown()

Reports that the execution engine has shutdown.

---

### Additional Sections

#### Interface ExecutionEnv

```java
public interface
ExecutionEnv
```

Functionality made available to a pluggable JShell execution engine. It is
provided to the execution engine by the core JShell implementation.

This interface is designed to provide the access to core JShell functionality
needed to implement ExecutionControl.

**Since:** 9
**See Also:** ExecutionControl

public interface

ExecutionEnv

Functionality made available to a pluggable JShell execution engine. It is
provided to the execution engine by the core JShell implementation.

This interface is designed to provide the access to core JShell functionality
needed to implement ExecutionControl.

This interface is designed to provide the access to core JShell functionality
needed to implement ExecutionControl.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

closeDown

()

Reports that the execution engine has shutdown.

List

<

String

>

extraRemoteVMOptions

()

Returns the additional VM options to be used when launching the remote
JVM.

PrintStream

userErr

()

Returns the user's error stream.

InputStream

userIn

()

Returns the user's input stream.

PrintStream

userOut

()

Returns the user's output stream.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

closeDown

()

Reports that the execution engine has shutdown.

List

<

String

>

extraRemoteVMOptions

()

Returns the additional VM options to be used when launching the remote
JVM.

PrintStream

userErr

()

Returns the user's error stream.

InputStream

userIn

()

Returns the user's input stream.

PrintStream

userOut

()

Returns the user's output stream.

---

#### Method Summary

Reports that the execution engine has shutdown.

Returns the additional VM options to be used when launching the remote
JVM.

Returns the user's error stream.

Returns the user's input stream.

Returns the user's output stream.

============ METHOD DETAIL ==========

- Method Detail

- userIn

```java
InputStream
userIn()
```

Returns the user's input stream.

**Returns:** the user's input stream

- userOut

```java
PrintStream
userOut()
```

Returns the user's output stream.

**Returns:** the user's output stream

- userErr

```java
PrintStream
userErr()
```

Returns the user's error stream.

**Returns:** the user's error stream

- extraRemoteVMOptions

```java
List
<
String
> extraRemoteVMOptions()
```

Returns the additional VM options to be used when launching the remote
JVM. This is advice to the execution engine.

Note: an execution engine need not launch a remote JVM.

**Returns:** the additional options with which to launch the remote JVM

- closeDown

```java
void closeDown()
```

Reports that the execution engine has shutdown.

Method Detail

- userIn

```java
InputStream
userIn()
```

Returns the user's input stream.

**Returns:** the user's input stream

- userOut

```java
PrintStream
userOut()
```

Returns the user's output stream.

**Returns:** the user's output stream

- userErr

```java
PrintStream
userErr()
```

Returns the user's error stream.

**Returns:** the user's error stream

- extraRemoteVMOptions

```java
List
<
String
> extraRemoteVMOptions()
```

Returns the additional VM options to be used when launching the remote
JVM. This is advice to the execution engine.

Note: an execution engine need not launch a remote JVM.

**Returns:** the additional options with which to launch the remote JVM

- closeDown

```java
void closeDown()
```

Reports that the execution engine has shutdown.

---

#### Method Detail

userIn

```java
InputStream
userIn()
```

Returns the user's input stream.

**Returns:** the user's input stream

---

#### userIn

InputStream

userIn()

Returns the user's input stream.

userOut

```java
PrintStream
userOut()
```

Returns the user's output stream.

**Returns:** the user's output stream

---

#### userOut

PrintStream

userOut()

Returns the user's output stream.

userErr

```java
PrintStream
userErr()
```

Returns the user's error stream.

**Returns:** the user's error stream

---

#### userErr

PrintStream

userErr()

Returns the user's error stream.

extraRemoteVMOptions

```java
List
<
String
> extraRemoteVMOptions()
```

Returns the additional VM options to be used when launching the remote
JVM. This is advice to the execution engine.

Note: an execution engine need not launch a remote JVM.

**Returns:** the additional options with which to launch the remote JVM

---

#### extraRemoteVMOptions

List

<

String

> extraRemoteVMOptions()

Returns the additional VM options to be used when launching the remote
JVM. This is advice to the execution engine.

Note: an execution engine need not launch a remote JVM.

Note: an execution engine need not launch a remote JVM.

closeDown

```java
void closeDown()
```

Reports that the execution engine has shutdown.

---

#### closeDown

void closeDown()

Reports that the execution engine has shutdown.

---

