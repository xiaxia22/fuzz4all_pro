# Interface ProcessHandle.Info

**Source:** `java.base\java\lang\ProcessHandle.Info.html`

### Class Description

```java
public static interface
ProcessHandle.Info
```

Information snapshot about the process.
The attributes of a process vary by operating system and are not available
in all implementations. Information about processes is limited
by the operating system privileges of the process making the request.
The return types are

Optional<T>

allowing explicit tests
and actions if the value is available.

**Enclosing interface:** ProcessHandle

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### Optional
<
String
> command()

Returns the executable pathname of the process.

**Returns:**
- an

Optional<String>

of the executable pathname
of the process

---

#### Optional
<
String
> commandLine()

Returns the command line of the process.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

**Returns:**
- an

Optional<String>

of the command line
of the process

**API Note:**
- Note that the returned executable pathname and the
arguments may be truncated on some platforms due to system
limitations.

The executable pathname may contain only the
name of the executable without the full path information.
It is undecideable whether white space separates different
arguments or is part of a single argument.

---

#### Optional
<
String
[]> arguments()

Returns an array of Strings of the arguments of the process.

**Returns:**
- an

Optional<String[]>

of the arguments of the process

**API Note:**
- On some platforms, native applications are free to change
the arguments array after startup and this method may only
show the changed values.

---

#### Optional
<
Instant
> startInstant()

Returns the start time of the process.

**Returns:**
- an

Optional<Instant>

of the start time of the process

---

#### Optional
<
Duration
> totalCpuDuration()

Returns the total cputime accumulated of the process.

**Returns:**
- an

Optional<Duration>

for the accumulated total cputime

---

#### Optional
<
String
> user()

Return the user of the process.

**Returns:**
- an

Optional<String>

for the user of the process

---

### Additional Sections

#### Interface ProcessHandle.Info

**Enclosing interface:** ProcessHandle

```java
public static interface
ProcessHandle.Info
```

Information snapshot about the process.
The attributes of a process vary by operating system and are not available
in all implementations. Information about processes is limited
by the operating system privileges of the process making the request.
The return types are

Optional<T>

allowing explicit tests
and actions if the value is available.

**Since:** 9

public static interface

ProcessHandle.Info

Information snapshot about the process.
The attributes of a process vary by operating system and are not available
in all implementations. Information about processes is limited
by the operating system privileges of the process making the request.
The return types are

Optional<T>

allowing explicit tests
and actions if the value is available.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Optional

<

String

[]>

arguments

()

Returns an array of Strings of the arguments of the process.

Optional

<

String

>

command

()

Returns the executable pathname of the process.

Optional

<

String

>

commandLine

()

Returns the command line of the process.

Optional

<

Instant

>

startInstant

()

Returns the start time of the process.

Optional

<

Duration

>

totalCpuDuration

()

Returns the total cputime accumulated of the process.

Optional

<

String

>

user

()

Return the user of the process.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

Optional

<

String

[]>

arguments

()

Returns an array of Strings of the arguments of the process.

Optional

<

String

>

command

()

Returns the executable pathname of the process.

Optional

<

String

>

commandLine

()

Returns the command line of the process.

Optional

<

Instant

>

startInstant

()

Returns the start time of the process.

Optional

<

Duration

>

totalCpuDuration

()

Returns the total cputime accumulated of the process.

Optional

<

String

>

user

()

Return the user of the process.

---

#### Method Summary

Returns an array of Strings of the arguments of the process.

Returns the executable pathname of the process.

Returns the command line of the process.

Returns the start time of the process.

Returns the total cputime accumulated of the process.

Return the user of the process.

============ METHOD DETAIL ==========

- Method Detail

- command

```java
Optional
<
String
> command()
```

Returns the executable pathname of the process.

**Returns:** an

Optional<String>

of the executable pathname
of the process

- commandLine

```java
Optional
<
String
> commandLine()
```

Returns the command line of the process.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

**API Note:** Note that the returned executable pathname and the
arguments may be truncated on some platforms due to system
limitations.

The executable pathname may contain only the
name of the executable without the full path information.
It is undecideable whether white space separates different
arguments or is part of a single argument.
**Returns:** an

Optional<String>

of the command line
of the process

- arguments

```java
Optional
<
String
[]> arguments()
```

Returns an array of Strings of the arguments of the process.

**API Note:** On some platforms, native applications are free to change
the arguments array after startup and this method may only
show the changed values.
**Returns:** an

Optional<String[]>

of the arguments of the process

- startInstant

```java
Optional
<
Instant
> startInstant()
```

Returns the start time of the process.

**Returns:** an

Optional<Instant>

of the start time of the process

- totalCpuDuration

```java
Optional
<
Duration
> totalCpuDuration()
```

Returns the total cputime accumulated of the process.

**Returns:** an

Optional<Duration>

for the accumulated total cputime

- user

```java
Optional
<
String
> user()
```

Return the user of the process.

**Returns:** an

Optional<String>

for the user of the process

Method Detail

- command

```java
Optional
<
String
> command()
```

Returns the executable pathname of the process.

**Returns:** an

Optional<String>

of the executable pathname
of the process

- commandLine

```java
Optional
<
String
> commandLine()
```

Returns the command line of the process.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

**API Note:** Note that the returned executable pathname and the
arguments may be truncated on some platforms due to system
limitations.

The executable pathname may contain only the
name of the executable without the full path information.
It is undecideable whether white space separates different
arguments or is part of a single argument.
**Returns:** an

Optional<String>

of the command line
of the process

- arguments

```java
Optional
<
String
[]> arguments()
```

Returns an array of Strings of the arguments of the process.

**API Note:** On some platforms, native applications are free to change
the arguments array after startup and this method may only
show the changed values.
**Returns:** an

Optional<String[]>

of the arguments of the process

- startInstant

```java
Optional
<
Instant
> startInstant()
```

Returns the start time of the process.

**Returns:** an

Optional<Instant>

of the start time of the process

- totalCpuDuration

```java
Optional
<
Duration
> totalCpuDuration()
```

Returns the total cputime accumulated of the process.

**Returns:** an

Optional<Duration>

for the accumulated total cputime

- user

```java
Optional
<
String
> user()
```

Return the user of the process.

**Returns:** an

Optional<String>

for the user of the process

---

#### Method Detail

command

```java
Optional
<
String
> command()
```

Returns the executable pathname of the process.

**Returns:** an

Optional<String>

of the executable pathname
of the process

---

#### command

Optional

<

String

> command()

Returns the executable pathname of the process.

commandLine

```java
Optional
<
String
> commandLine()
```

Returns the command line of the process.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

**API Note:** Note that the returned executable pathname and the
arguments may be truncated on some platforms due to system
limitations.

The executable pathname may contain only the
name of the executable without the full path information.
It is undecideable whether white space separates different
arguments or is part of a single argument.
**Returns:** an

Optional<String>

of the command line
of the process

---

#### commandLine

Optional

<

String

> commandLine()

Returns the command line of the process.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

If

command()

and

arguments()

return
non-empty optionals, this is simply a convenience method which concatenates
the values of the two functions separated by spaces. Otherwise it will return a
best-effort, platform dependent representation of the command line.

The executable pathname may contain only the
name of the executable without the full path information.
It is undecideable whether white space separates different
arguments or is part of a single argument.

arguments

```java
Optional
<
String
[]> arguments()
```

Returns an array of Strings of the arguments of the process.

**API Note:** On some platforms, native applications are free to change
the arguments array after startup and this method may only
show the changed values.
**Returns:** an

Optional<String[]>

of the arguments of the process

---

#### arguments

Optional

<

String

[]> arguments()

Returns an array of Strings of the arguments of the process.

startInstant

```java
Optional
<
Instant
> startInstant()
```

Returns the start time of the process.

**Returns:** an

Optional<Instant>

of the start time of the process

---

#### startInstant

Optional

<

Instant

> startInstant()

Returns the start time of the process.

totalCpuDuration

```java
Optional
<
Duration
> totalCpuDuration()
```

Returns the total cputime accumulated of the process.

**Returns:** an

Optional<Duration>

for the accumulated total cputime

---

#### totalCpuDuration

Optional

<

Duration

> totalCpuDuration()

Returns the total cputime accumulated of the process.

user

```java
Optional
<
String
> user()
```

Return the user of the process.

**Returns:** an

Optional<String>

for the user of the process

---

#### user

Optional

<

String

> user()

Return the user of the process.

---

