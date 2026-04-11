# Interface JavaShellToolBuilder

**Source:** `jdk.jshell\jdk\jshell\tool\JavaShellToolBuilder.html`

### Class Description

```java
public interface
JavaShellToolBuilder
```

Interface to configure and run a Java shell tool instance. An instance of the
builder is created with the static

builder()

method. This builder can,
optionally, be configured with the configuration methods. All configuration
methods return the builder instance for use in chained initialization. All
configuration methods have sensible defaults which will be used if they are
not called.. After zero or more calls to configuration methods, the tool is
launched with a call to

run(java.lang.String...)

.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### static
JavaShellToolBuilder
builder()

Create a builder for launching the JDK jshell tool.

**Returns:**
- a builder which can be used to configure and launch the jshell
tool

---

#### JavaShellToolBuilder
in​(
InputStream
cmdIn,

InputStream
userIn)

Set the input channels.

**Parameters:**
- cmdIn

- source of command input
- userIn

- source of input for running user code, or

null

to
extract user input from cmdIn

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If this method is not called, the behavior should be
equivalent to calling

in(System.in, null)

.

---

#### JavaShellToolBuilder
out​(
PrintStream
output)

Set the output channels. Same as

out(output, output, output)

.

**Parameters:**
- output

- destination of command feedback, console interaction, and
user code output

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out)

.

---

#### JavaShellToolBuilder
out​(
PrintStream
cmdOut,

PrintStream
console,

PrintStream
userOut)

Set the output channels.

**Parameters:**
- cmdOut

- destination of command feedback including error messages
for users
- console

- destination of console interaction
- userOut

- destination of user code output. For example, user snippet

System.out.println("Hello")

when executed

Hello

goes to
userOut.

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out, System.out, System.out)

.

---

#### JavaShellToolBuilder
err​(
PrintStream
error)

Set the error channels. Same as

err(error, error)

.

**Parameters:**
- error

- destination of tool errors, and
user code errors

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err)

.

---

#### JavaShellToolBuilder
err​(
PrintStream
cmdErr,

PrintStream
userErr)

Set the error channels.

**Parameters:**
- cmdErr

- destination of tool start-up and fatal errors
- userErr

- destination of user code error output.
For example, user snippet

System.err.println("Oops")

when executed

Oops

goes to userErr.

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err, System.err, System.err)

.

---

#### JavaShellToolBuilder
persistence​(
Preferences
prefs)

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Parameters:**
- prefs

- an instance of

Preferences

that
is used to retrieve and store persistent information

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.

---

#### JavaShellToolBuilder
persistence​(
Map
<
String
,​
String
> prefsMap)

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Parameters:**
- prefsMap

- an instance of

Map

that
is used to retrieve and store persistent information

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.

---

#### JavaShellToolBuilder
env​(
Map
<
String
,​
String
> vars)

Set the source for environment variables.

**Parameters:**
- vars

- the Map of environment variable names to values

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If this method is not called, the behavior should be
equivalent to calling

env(System.getenv())

.

---

#### JavaShellToolBuilder
locale​(
Locale
locale)

Set the locale.

**Parameters:**
- locale

- the locale

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If this method is not called, the behavior should be
equivalent to calling

locale(Locale.getDefault())

.

---

#### JavaShellToolBuilder
promptCapture​(boolean capture)

Set to enable a command capturing prompt override.

**Parameters:**
- capture

- if

true

, basic prompt is the

ENQ

character and continuation prompt is the

ACK

character.
If false, prompts are as set with set-up or user

/set

commands.

**Returns:**
- the

JavaShellToolBuilder

instance

**Implementation Requirements:**
- If this method is not called, the behavior should be
equivalent to calling

promptCapture(false)

.

---

#### void run​(
String
... arguments)
throws
Exception

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder. The exit code from
the Java shell tool is ignored.

**Parameters:**
- arguments

- the command-line arguments (including options), if any

**Throws:**
- Exception

- an unexpected fatal exception

---

#### default int start​(
String
... arguments)
throws
Exception

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder.

**Parameters:**
- arguments

- the command-line arguments (including options), if any

**Returns:**
- the exit status with which the tool explicitly exited (if any),
otherwise 0 for success or 1 for failure

**Throws:**
- Exception

- an unexpected fatal exception

**Implementation Requirements:**
- The default implementation always returns zero. Implementations
of this interface should override this method, returning the exit status.

---

### Additional Sections

#### Interface JavaShellToolBuilder

```java
public interface
JavaShellToolBuilder
```

Interface to configure and run a Java shell tool instance. An instance of the
builder is created with the static

builder()

method. This builder can,
optionally, be configured with the configuration methods. All configuration
methods return the builder instance for use in chained initialization. All
configuration methods have sensible defaults which will be used if they are
not called.. After zero or more calls to configuration methods, the tool is
launched with a call to

run(java.lang.String...)

.

**Since:** 9

public interface

JavaShellToolBuilder

Interface to configure and run a Java shell tool instance. An instance of the
builder is created with the static

builder()

method. This builder can,
optionally, be configured with the configuration methods. All configuration
methods return the builder instance for use in chained initialization. All
configuration methods have sensible defaults which will be used if they are
not called.. After zero or more calls to configuration methods, the tool is
launched with a call to

run(java.lang.String...)

.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

static

JavaShellToolBuilder

builder

()

Create a builder for launching the JDK jshell tool.

JavaShellToolBuilder

env

​(

Map

<

String

,​

String

> vars)

Set the source for environment variables.

JavaShellToolBuilder

err

​(

PrintStream

error)

Set the error channels.

JavaShellToolBuilder

err

​(

PrintStream

cmdErr,

PrintStream

userErr)

Set the error channels.

JavaShellToolBuilder

in

​(

InputStream

cmdIn,

InputStream

userIn)

Set the input channels.

JavaShellToolBuilder

locale

​(

Locale

locale)

Set the locale.

JavaShellToolBuilder

out

​(

PrintStream

output)

Set the output channels.

JavaShellToolBuilder

out

​(

PrintStream

cmdOut,

PrintStream

console,

PrintStream

userOut)

Set the output channels.

JavaShellToolBuilder

persistence

​(

Map

<

String

,​

String

> prefsMap)

Set the storage mechanism for persistent information which includes
input history and retained settings.

JavaShellToolBuilder

persistence

​(

Preferences

prefs)

Set the storage mechanism for persistent information which includes
input history and retained settings.

JavaShellToolBuilder

promptCapture

​(boolean capture)

Set to enable a command capturing prompt override.

void

run

​(

String

... arguments)

Run an instance of the Java shell tool as configured by the other methods
in this interface.

default int

start

​(

String

... arguments)

Run an instance of the Java shell tool as configured by the other methods
in this interface.

Method Summary

All Methods

Static Methods

Instance Methods

Abstract Methods

Default Methods

Modifier and Type

Method

Description

static

JavaShellToolBuilder

builder

()

Create a builder for launching the JDK jshell tool.

JavaShellToolBuilder

env

​(

Map

<

String

,​

String

> vars)

Set the source for environment variables.

JavaShellToolBuilder

err

​(

PrintStream

error)

Set the error channels.

JavaShellToolBuilder

err

​(

PrintStream

cmdErr,

PrintStream

userErr)

Set the error channels.

JavaShellToolBuilder

in

​(

InputStream

cmdIn,

InputStream

userIn)

Set the input channels.

JavaShellToolBuilder

locale

​(

Locale

locale)

Set the locale.

JavaShellToolBuilder

out

​(

PrintStream

output)

Set the output channels.

JavaShellToolBuilder

out

​(

PrintStream

cmdOut,

PrintStream

console,

PrintStream

userOut)

Set the output channels.

JavaShellToolBuilder

persistence

​(

Map

<

String

,​

String

> prefsMap)

Set the storage mechanism for persistent information which includes
input history and retained settings.

JavaShellToolBuilder

persistence

​(

Preferences

prefs)

Set the storage mechanism for persistent information which includes
input history and retained settings.

JavaShellToolBuilder

promptCapture

​(boolean capture)

Set to enable a command capturing prompt override.

void

run

​(

String

... arguments)

Run an instance of the Java shell tool as configured by the other methods
in this interface.

default int

start

​(

String

... arguments)

Run an instance of the Java shell tool as configured by the other methods
in this interface.

---

#### Method Summary

Create a builder for launching the JDK jshell tool.

Set the source for environment variables.

Set the error channels.

Set the input channels.

Set the locale.

Set the output channels.

Set the storage mechanism for persistent information which includes
input history and retained settings.

Set to enable a command capturing prompt override.

Run an instance of the Java shell tool as configured by the other methods
in this interface.

============ METHOD DETAIL ==========

- Method Detail

- builder

```java
static
JavaShellToolBuilder
builder()
```

Create a builder for launching the JDK jshell tool.

**Returns:** a builder which can be used to configure and launch the jshell
tool

- in

```java
JavaShellToolBuilder
in​(
InputStream
cmdIn,

InputStream
userIn)
```

Set the input channels.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

in(System.in, null)

.
**Parameters:** cmdIn

- source of command input
**Parameters:** userIn

- source of input for running user code, or

null

to
extract user input from cmdIn
**Returns:** the

JavaShellToolBuilder

instance

- out

```java
JavaShellToolBuilder
out​(
PrintStream
output)
```

Set the output channels. Same as

out(output, output, output)

.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out)

.
**Parameters:** output

- destination of command feedback, console interaction, and
user code output
**Returns:** the

JavaShellToolBuilder

instance

- out

```java
JavaShellToolBuilder
out​(
PrintStream
cmdOut,

PrintStream
console,

PrintStream
userOut)
```

Set the output channels.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out, System.out, System.out)

.
**Parameters:** cmdOut

- destination of command feedback including error messages
for users
**Parameters:** console

- destination of console interaction
**Parameters:** userOut

- destination of user code output. For example, user snippet

System.out.println("Hello")

when executed

Hello

goes to
userOut.
**Returns:** the

JavaShellToolBuilder

instance

- err

```java
JavaShellToolBuilder
err​(
PrintStream
error)
```

Set the error channels. Same as

err(error, error)

.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err)

.
**Parameters:** error

- destination of tool errors, and
user code errors
**Returns:** the

JavaShellToolBuilder

instance

- err

```java
JavaShellToolBuilder
err​(
PrintStream
cmdErr,

PrintStream
userErr)
```

Set the error channels.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err, System.err, System.err)

.
**Parameters:** cmdErr

- destination of tool start-up and fatal errors
**Parameters:** userErr

- destination of user code error output.
For example, user snippet

System.err.println("Oops")

when executed

Oops

goes to userErr.
**Returns:** the

JavaShellToolBuilder

instance

- persistence

```java
JavaShellToolBuilder
persistence​(
Preferences
prefs)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefs

- an instance of

Preferences

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

- persistence

```java
JavaShellToolBuilder
persistence​(
Map
<
String
,​
String
> prefsMap)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefsMap

- an instance of

Map

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

- env

```java
JavaShellToolBuilder
env​(
Map
<
String
,​
String
> vars)
```

Set the source for environment variables.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

env(System.getenv())

.
**Parameters:** vars

- the Map of environment variable names to values
**Returns:** the

JavaShellToolBuilder

instance

- locale

```java
JavaShellToolBuilder
locale​(
Locale
locale)
```

Set the locale.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

locale(Locale.getDefault())

.
**Parameters:** locale

- the locale
**Returns:** the

JavaShellToolBuilder

instance

- promptCapture

```java
JavaShellToolBuilder
promptCapture​(boolean capture)
```

Set to enable a command capturing prompt override.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

promptCapture(false)

.
**Parameters:** capture

- if

true

, basic prompt is the

ENQ

character and continuation prompt is the

ACK

character.
If false, prompts are as set with set-up or user

/set

commands.
**Returns:** the

JavaShellToolBuilder

instance

- run

```java
void run​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder. The exit code from
the Java shell tool is ignored.

**Parameters:** arguments

- the command-line arguments (including options), if any
**Throws:** Exception

- an unexpected fatal exception

- start

```java
default int start​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder.

**Implementation Requirements:** The default implementation always returns zero. Implementations
of this interface should override this method, returning the exit status.
**Parameters:** arguments

- the command-line arguments (including options), if any
**Returns:** the exit status with which the tool explicitly exited (if any),
otherwise 0 for success or 1 for failure
**Throws:** Exception

- an unexpected fatal exception

Method Detail

- builder

```java
static
JavaShellToolBuilder
builder()
```

Create a builder for launching the JDK jshell tool.

**Returns:** a builder which can be used to configure and launch the jshell
tool

- in

```java
JavaShellToolBuilder
in​(
InputStream
cmdIn,

InputStream
userIn)
```

Set the input channels.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

in(System.in, null)

.
**Parameters:** cmdIn

- source of command input
**Parameters:** userIn

- source of input for running user code, or

null

to
extract user input from cmdIn
**Returns:** the

JavaShellToolBuilder

instance

- out

```java
JavaShellToolBuilder
out​(
PrintStream
output)
```

Set the output channels. Same as

out(output, output, output)

.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out)

.
**Parameters:** output

- destination of command feedback, console interaction, and
user code output
**Returns:** the

JavaShellToolBuilder

instance

- out

```java
JavaShellToolBuilder
out​(
PrintStream
cmdOut,

PrintStream
console,

PrintStream
userOut)
```

Set the output channels.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out, System.out, System.out)

.
**Parameters:** cmdOut

- destination of command feedback including error messages
for users
**Parameters:** console

- destination of console interaction
**Parameters:** userOut

- destination of user code output. For example, user snippet

System.out.println("Hello")

when executed

Hello

goes to
userOut.
**Returns:** the

JavaShellToolBuilder

instance

- err

```java
JavaShellToolBuilder
err​(
PrintStream
error)
```

Set the error channels. Same as

err(error, error)

.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err)

.
**Parameters:** error

- destination of tool errors, and
user code errors
**Returns:** the

JavaShellToolBuilder

instance

- err

```java
JavaShellToolBuilder
err​(
PrintStream
cmdErr,

PrintStream
userErr)
```

Set the error channels.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err, System.err, System.err)

.
**Parameters:** cmdErr

- destination of tool start-up and fatal errors
**Parameters:** userErr

- destination of user code error output.
For example, user snippet

System.err.println("Oops")

when executed

Oops

goes to userErr.
**Returns:** the

JavaShellToolBuilder

instance

- persistence

```java
JavaShellToolBuilder
persistence​(
Preferences
prefs)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefs

- an instance of

Preferences

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

- persistence

```java
JavaShellToolBuilder
persistence​(
Map
<
String
,​
String
> prefsMap)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefsMap

- an instance of

Map

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

- env

```java
JavaShellToolBuilder
env​(
Map
<
String
,​
String
> vars)
```

Set the source for environment variables.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

env(System.getenv())

.
**Parameters:** vars

- the Map of environment variable names to values
**Returns:** the

JavaShellToolBuilder

instance

- locale

```java
JavaShellToolBuilder
locale​(
Locale
locale)
```

Set the locale.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

locale(Locale.getDefault())

.
**Parameters:** locale

- the locale
**Returns:** the

JavaShellToolBuilder

instance

- promptCapture

```java
JavaShellToolBuilder
promptCapture​(boolean capture)
```

Set to enable a command capturing prompt override.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

promptCapture(false)

.
**Parameters:** capture

- if

true

, basic prompt is the

ENQ

character and continuation prompt is the

ACK

character.
If false, prompts are as set with set-up or user

/set

commands.
**Returns:** the

JavaShellToolBuilder

instance

- run

```java
void run​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder. The exit code from
the Java shell tool is ignored.

**Parameters:** arguments

- the command-line arguments (including options), if any
**Throws:** Exception

- an unexpected fatal exception

- start

```java
default int start​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder.

**Implementation Requirements:** The default implementation always returns zero. Implementations
of this interface should override this method, returning the exit status.
**Parameters:** arguments

- the command-line arguments (including options), if any
**Returns:** the exit status with which the tool explicitly exited (if any),
otherwise 0 for success or 1 for failure
**Throws:** Exception

- an unexpected fatal exception

---

#### Method Detail

builder

```java
static
JavaShellToolBuilder
builder()
```

Create a builder for launching the JDK jshell tool.

**Returns:** a builder which can be used to configure and launch the jshell
tool

---

#### builder

static

JavaShellToolBuilder

builder()

Create a builder for launching the JDK jshell tool.

in

```java
JavaShellToolBuilder
in​(
InputStream
cmdIn,

InputStream
userIn)
```

Set the input channels.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

in(System.in, null)

.
**Parameters:** cmdIn

- source of command input
**Parameters:** userIn

- source of input for running user code, or

null

to
extract user input from cmdIn
**Returns:** the

JavaShellToolBuilder

instance

---

#### in

JavaShellToolBuilder

in​(

InputStream

cmdIn,

InputStream

userIn)

Set the input channels.

out

```java
JavaShellToolBuilder
out​(
PrintStream
output)
```

Set the output channels. Same as

out(output, output, output)

.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out)

.
**Parameters:** output

- destination of command feedback, console interaction, and
user code output
**Returns:** the

JavaShellToolBuilder

instance

---

#### out

JavaShellToolBuilder

out​(

PrintStream

output)

Set the output channels. Same as

out(output, output, output)

.

out

```java
JavaShellToolBuilder
out​(
PrintStream
cmdOut,

PrintStream
console,

PrintStream
userOut)
```

Set the output channels.

**Implementation Requirements:** If neither

out

method is called, the behavior should be
equivalent to calling

out(System.out, System.out, System.out)

.
**Parameters:** cmdOut

- destination of command feedback including error messages
for users
**Parameters:** console

- destination of console interaction
**Parameters:** userOut

- destination of user code output. For example, user snippet

System.out.println("Hello")

when executed

Hello

goes to
userOut.
**Returns:** the

JavaShellToolBuilder

instance

---

#### out

JavaShellToolBuilder

out​(

PrintStream

cmdOut,

PrintStream

console,

PrintStream

userOut)

Set the output channels.

err

```java
JavaShellToolBuilder
err​(
PrintStream
error)
```

Set the error channels. Same as

err(error, error)

.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err)

.
**Parameters:** error

- destination of tool errors, and
user code errors
**Returns:** the

JavaShellToolBuilder

instance

---

#### err

JavaShellToolBuilder

err​(

PrintStream

error)

Set the error channels. Same as

err(error, error)

.

err

```java
JavaShellToolBuilder
err​(
PrintStream
cmdErr,

PrintStream
userErr)
```

Set the error channels.

**Implementation Requirements:** If neither

err

method is called, the behavior should be
equivalent to calling

err(System.err, System.err, System.err)

.
**Parameters:** cmdErr

- destination of tool start-up and fatal errors
**Parameters:** userErr

- destination of user code error output.
For example, user snippet

System.err.println("Oops")

when executed

Oops

goes to userErr.
**Returns:** the

JavaShellToolBuilder

instance

---

#### err

JavaShellToolBuilder

err​(

PrintStream

cmdErr,

PrintStream

userErr)

Set the error channels.

persistence

```java
JavaShellToolBuilder
persistence​(
Preferences
prefs)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefs

- an instance of

Preferences

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

---

#### persistence

JavaShellToolBuilder

persistence​(

Preferences

prefs)

Set the storage mechanism for persistent information which includes
input history and retained settings.

persistence

```java
JavaShellToolBuilder
persistence​(
Map
<
String
,​
String
> prefsMap)
```

Set the storage mechanism for persistent information which includes
input history and retained settings.

**Implementation Requirements:** If neither

persistence

method is called, the behavior
should be to use the tool's standard persistence mechanism.
**Parameters:** prefsMap

- an instance of

Map

that
is used to retrieve and store persistent information
**Returns:** the

JavaShellToolBuilder

instance

---

#### persistence

JavaShellToolBuilder

persistence​(

Map

<

String

,​

String

> prefsMap)

Set the storage mechanism for persistent information which includes
input history and retained settings.

env

```java
JavaShellToolBuilder
env​(
Map
<
String
,​
String
> vars)
```

Set the source for environment variables.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

env(System.getenv())

.
**Parameters:** vars

- the Map of environment variable names to values
**Returns:** the

JavaShellToolBuilder

instance

---

#### env

JavaShellToolBuilder

env​(

Map

<

String

,​

String

> vars)

Set the source for environment variables.

locale

```java
JavaShellToolBuilder
locale​(
Locale
locale)
```

Set the locale.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

locale(Locale.getDefault())

.
**Parameters:** locale

- the locale
**Returns:** the

JavaShellToolBuilder

instance

---

#### locale

JavaShellToolBuilder

locale​(

Locale

locale)

Set the locale.

promptCapture

```java
JavaShellToolBuilder
promptCapture​(boolean capture)
```

Set to enable a command capturing prompt override.

**Implementation Requirements:** If this method is not called, the behavior should be
equivalent to calling

promptCapture(false)

.
**Parameters:** capture

- if

true

, basic prompt is the

ENQ

character and continuation prompt is the

ACK

character.
If false, prompts are as set with set-up or user

/set

commands.
**Returns:** the

JavaShellToolBuilder

instance

---

#### promptCapture

JavaShellToolBuilder

promptCapture​(boolean capture)

Set to enable a command capturing prompt override.

run

```java
void run​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder. The exit code from
the Java shell tool is ignored.

**Parameters:** arguments

- the command-line arguments (including options), if any
**Throws:** Exception

- an unexpected fatal exception

---

#### run

void run​(

String

... arguments)
throws

Exception

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder. The exit code from
the Java shell tool is ignored.

start

```java
default int start​(
String
... arguments)
throws
Exception
```

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder.

**Implementation Requirements:** The default implementation always returns zero. Implementations
of this interface should override this method, returning the exit status.
**Parameters:** arguments

- the command-line arguments (including options), if any
**Returns:** the exit status with which the tool explicitly exited (if any),
otherwise 0 for success or 1 for failure
**Throws:** Exception

- an unexpected fatal exception

---

#### start

default int start​(

String

... arguments)
throws

Exception

Run an instance of the Java shell tool as configured by the other methods
in this interface. This call is not destructive, more than one call of
this method may be made from a configured builder.

---

