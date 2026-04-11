# Class Console

**Source:** `java.base\java\io\Console.html`

### Class Description

```java
public final class
Console

extends
Object

implements
Flushable
```

Methods to access the character-based console device, if any, associated
with the current Java virtual machine.

Whether a virtual machine has a console is dependent upon the
underlying platform and also upon the manner in which the virtual
machine is invoked. If the virtual machine is started from an
interactive command line without redirecting the standard input and
output streams then its console will exist and will typically be
connected to the keyboard and display from which the virtual machine
was launched. If the virtual machine is started automatically, for
example by a background job scheduler, then it will typically not
have a console.

If this virtual machine has a console then it is represented by a
unique instance of this class which can be obtained by invoking the

System.console()

method. If no console device is
available then an invocation of that method will return

null

.

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

**All Implemented Interfaces:** Flushable

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public
PrintWriter
writer()

Retrieves the unique

PrintWriter

object
associated with this console.

**Returns:**
- The printwriter associated with this console

---

#### public
Reader
reader()

Retrieves the unique

Reader

object associated
with this console.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

**Returns:**
- The reader associated with this console

---

#### public
Console
format​(
String
fmt,

Object
... args)

Writes a formatted string to this console's output stream using
the specified format string and arguments.

**Parameters:**
- fmt

- A format string as described in

Format string syntax
- args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.

**Returns:**
- This console

**Throws:**
- IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.

---

#### public
Console
printf​(
String
format,

Object
... args)

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

**Parameters:**
- format

- A format string as described in

Format string syntax

.
- args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.

**Returns:**
- This console

**Throws:**
- IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the
formatter class specification.

---

#### public
String
readLine​(
String
fmt,

Object
... args)

Provides a formatted prompt, then reads a single line of text from the
console.

**Parameters:**
- fmt

- A format string as described in

Format string syntax

.
- args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.

**Returns:**
- A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.

**Throws:**
- IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.
- IOError

- If an I/O error occurs.

---

#### public
String
readLine()

Reads a single line of text from the console.

**Returns:**
- A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.

**Throws:**
- IOError

- If an I/O error occurs.

---

#### public char[] readPassword​(
String
fmt,

Object
... args)

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

**Parameters:**
- fmt

- A format string as described in

Format string syntax

for the prompt text.
- args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.

**Returns:**
- A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.

**Throws:**
- IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the formatter class specification.
- IOError

- If an I/O error occurs.

---

#### public char[] readPassword()

Reads a password or passphrase from the console with echoing disabled

**Returns:**
- A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.

**Throws:**
- IOError

- If an I/O error occurs.

---

#### public void flush()

Flushes the console and forces any buffered output to be written
immediately .

**Specified by:**
- flush

in interface

Flushable

---

### Additional Sections

#### Class Console

java.lang.Object

- java.io.Console

java.io.Console

**All Implemented Interfaces:** Flushable

```java
public final class
Console

extends
Object

implements
Flushable
```

Methods to access the character-based console device, if any, associated
with the current Java virtual machine.

Whether a virtual machine has a console is dependent upon the
underlying platform and also upon the manner in which the virtual
machine is invoked. If the virtual machine is started from an
interactive command line without redirecting the standard input and
output streams then its console will exist and will typically be
connected to the keyboard and display from which the virtual machine
was launched. If the virtual machine is started automatically, for
example by a background job scheduler, then it will typically not
have a console.

If this virtual machine has a console then it is represented by a
unique instance of this class which can be obtained by invoking the

System.console()

method. If no console device is
available then an invocation of that method will return

null

.

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

**Since:** 1.6

public final class

Console

extends

Object

implements

Flushable

Methods to access the character-based console device, if any, associated
with the current Java virtual machine.

Whether a virtual machine has a console is dependent upon the
underlying platform and also upon the manner in which the virtual
machine is invoked. If the virtual machine is started from an
interactive command line without redirecting the standard input and
output streams then its console will exist and will typically be
connected to the keyboard and display from which the virtual machine
was launched. If the virtual machine is started automatically, for
example by a background job scheduler, then it will typically not
have a console.

If this virtual machine has a console then it is represented by a
unique instance of this class which can be obtained by invoking the

System.console()

method. If no console device is
available then an invocation of that method will return

null

.

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Whether a virtual machine has a console is dependent upon the
underlying platform and also upon the manner in which the virtual
machine is invoked. If the virtual machine is started from an
interactive command line without redirecting the standard input and
output streams then its console will exist and will typically be
connected to the keyboard and display from which the virtual machine
was launched. If the virtual machine is started automatically, for
example by a background job scheduler, then it will typically not
have a console.

If this virtual machine has a console then it is represented by a
unique instance of this class which can be obtained by invoking the

System.console()

method. If no console device is
available then an invocation of that method will return

null

.

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

If this virtual machine has a console then it is represented by a
unique instance of this class which can be obtained by invoking the

System.console()

method. If no console device is
available then an invocation of that method will return

null

.

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Read and write operations are synchronized to guarantee the atomic
completion of critical operations; therefore invoking methods

readLine()

,

readPassword()

,

format()

,

printf()

as well as the read, format and write operations
on the objects returned by

reader()

and

writer()

may
block in multithreaded scenarios.

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Invoking

close()

on the objects returned by the

reader()

and the

writer()

will not close the underlying stream of those
objects.

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

The console-read methods return

null

when the end of the
console input stream is reached, for example by typing control-D on
Unix or control-Z on Windows. Subsequent read operations will succeed
if additional characters are later entered on the console's input
device.

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Unless otherwise specified, passing a

null

argument to any method
in this class will cause a

NullPointerException

to be thrown.

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Security note:

If an application needs to read a password or other secure data, it should
use

readPassword()

or

readPassword(String, Object...)

and
manually zero the returned character array after processing to minimize the
lifetime of sensitive data in memory.

```java
Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}
```

Console cons;
char[] passwd;
if ((cons = System.console()) != null &&
(passwd = cons.readPassword("[%s]", "Password:")) != null) {
...
java.util.Arrays.fill(passwd, ' ');
}

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes the console and forces any buffered output to be written
immediately .

Console

format

​(

String

fmt,

Object

... args)

Writes a formatted string to this console's output stream using
the specified format string and arguments.

Console

printf

​(

String

format,

Object

... args)

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

Reader

reader

()

Retrieves the unique

Reader

object associated
with this console.

String

readLine

()

Reads a single line of text from the console.

String

readLine

​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a single line of text from the
console.

char[]

readPassword

()

Reads a password or passphrase from the console with echoing disabled

char[]

readPassword

​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

PrintWriter

writer

()

Retrieves the unique

PrintWriter

object
associated with this console.

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

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

void

flush

()

Flushes the console and forces any buffered output to be written
immediately .

Console

format

​(

String

fmt,

Object

... args)

Writes a formatted string to this console's output stream using
the specified format string and arguments.

Console

printf

​(

String

format,

Object

... args)

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

Reader

reader

()

Retrieves the unique

Reader

object associated
with this console.

String

readLine

()

Reads a single line of text from the console.

String

readLine

​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a single line of text from the
console.

char[]

readPassword

()

Reads a password or passphrase from the console with echoing disabled

char[]

readPassword

​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

PrintWriter

writer

()

Retrieves the unique

PrintWriter

object
associated with this console.

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

Flushes the console and forces any buffered output to be written
immediately .

Writes a formatted string to this console's output stream using
the specified format string and arguments.

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

Retrieves the unique

Reader

object associated
with this console.

Reads a single line of text from the console.

Provides a formatted prompt, then reads a single line of text from the
console.

Reads a password or passphrase from the console with echoing disabled

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

Retrieves the unique

PrintWriter

object
associated with this console.

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

============ METHOD DETAIL ==========

- Method Detail

- writer

```java
public
PrintWriter
writer()
```

Retrieves the unique

PrintWriter

object
associated with this console.

**Returns:** The printwriter associated with this console

- reader

```java
public
Reader
reader()
```

Retrieves the unique

Reader

object associated
with this console.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

**Returns:** The reader associated with this console

- format

```java
public
Console
format​(
String
fmt,

Object
... args)
```

Writes a formatted string to this console's output stream using
the specified format string and arguments.

**Parameters:** fmt

- A format string as described in

Format string syntax
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.

- printf

```java
public
Console
printf​(
String
format,

Object
... args)
```

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

**Parameters:** format

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the
formatter class specification.

- readLine

```java
public
String
readLine​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a single line of text from the
console.

**Parameters:** fmt

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

- readLine

```java
public
String
readLine()
```

Reads a single line of text from the console.

**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

- readPassword

```java
public char[] readPassword​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

**Parameters:** fmt

- A format string as described in

Format string syntax

for the prompt text.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

- readPassword

```java
public char[] readPassword()
```

Reads a password or passphrase from the console with echoing disabled

**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

- flush

```java
public void flush()
```

Flushes the console and forces any buffered output to be written
immediately .

**Specified by:** flush

in interface

Flushable

Method Detail

- writer

```java
public
PrintWriter
writer()
```

Retrieves the unique

PrintWriter

object
associated with this console.

**Returns:** The printwriter associated with this console

- reader

```java
public
Reader
reader()
```

Retrieves the unique

Reader

object associated
with this console.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

**Returns:** The reader associated with this console

- format

```java
public
Console
format​(
String
fmt,

Object
... args)
```

Writes a formatted string to this console's output stream using
the specified format string and arguments.

**Parameters:** fmt

- A format string as described in

Format string syntax
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.

- printf

```java
public
Console
printf​(
String
format,

Object
... args)
```

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

**Parameters:** format

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the
formatter class specification.

- readLine

```java
public
String
readLine​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a single line of text from the
console.

**Parameters:** fmt

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

- readLine

```java
public
String
readLine()
```

Reads a single line of text from the console.

**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

- readPassword

```java
public char[] readPassword​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

**Parameters:** fmt

- A format string as described in

Format string syntax

for the prompt text.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

- readPassword

```java
public char[] readPassword()
```

Reads a password or passphrase from the console with echoing disabled

**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

- flush

```java
public void flush()
```

Flushes the console and forces any buffered output to be written
immediately .

**Specified by:** flush

in interface

Flushable

---

#### Method Detail

writer

```java
public
PrintWriter
writer()
```

Retrieves the unique

PrintWriter

object
associated with this console.

**Returns:** The printwriter associated with this console

---

#### writer

public

PrintWriter

writer()

Retrieves the unique

PrintWriter

object
associated with this console.

reader

```java
public
Reader
reader()
```

Retrieves the unique

Reader

object associated
with this console.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

**Returns:** The reader associated with this console

---

#### reader

public

Reader

reader()

Retrieves the unique

Reader

object associated
with this console.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

This method is intended to be used by sophisticated applications, for
example, a

Scanner

object which utilizes the rich
parsing/scanning functionality provided by the

Scanner

:

```java
Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}
```

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

Console con = System.console();
if (con != null) {
Scanner sc = new Scanner(con.reader());
...
}

For simple applications requiring only line-oriented reading, use

readLine(java.lang.String, java.lang.Object...)

.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

The bulk read operations

read(char[])

,

read(char[], int, int)

and

read(java.nio.CharBuffer)

on the returned object will not read in characters beyond the line
bound for each invocation, even if the destination buffer has space for
more characters. The

Reader

's

read

methods may block if a
line bound has not been entered or reached on the console's input device.
A line bound is considered to be any one of a line feed (

'\n'

),
a carriage return (

'\r'

), a carriage return followed immediately
by a linefeed, or an end of stream.

format

```java
public
Console
format​(
String
fmt,

Object
... args)
```

Writes a formatted string to this console's output stream using
the specified format string and arguments.

**Parameters:** fmt

- A format string as described in

Format string syntax
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.

---

#### format

public

Console

format​(

String

fmt,

Object

... args)

Writes a formatted string to this console's output stream using
the specified format string and arguments.

printf

```java
public
Console
printf​(
String
format,

Object
... args)
```

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

**Parameters:** format

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The number of arguments is
variable and may be zero. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
The behaviour on a

null

argument depends on the

conversion

.
**Returns:** This console
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the
formatter class specification.

---

#### printf

public

Console

printf​(

String

format,

Object

... args)

A convenience method to write a formatted string to this console's
output stream using the specified format string and arguments.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

An invocation of this method of the form

con.printf(format, args)

behaves in exactly the same way
as the invocation of

```java
con.format(format, args)
```

.

con.format(format, args)

readLine

```java
public
String
readLine​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a single line of text from the
console.

**Parameters:** fmt

- A format string as described in

Format string syntax

.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section
of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

---

#### readLine

public

String

readLine​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a single line of text from the
console.

readLine

```java
public
String
readLine()
```

Reads a single line of text from the console.

**Returns:** A string containing the line read from the console, not
including any line-termination characters, or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

---

#### readLine

public

String

readLine()

Reads a single line of text from the console.

readPassword

```java
public char[] readPassword​(
String
fmt,

Object
... args)
```

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

**Parameters:** fmt

- A format string as described in

Format string syntax

for the prompt text.
**Parameters:** args

- Arguments referenced by the format specifiers in the format
string. If there are more arguments than format specifiers, the
extra arguments are ignored. The maximum number of arguments is
limited by the maximum dimension of a Java array as defined by

The Java™ Virtual Machine Specification

.
**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IllegalFormatException

- If a format string contains an illegal syntax, a format
specifier that is incompatible with the given arguments,
insufficient arguments given the format string, or other
illegal conditions. For specification of all possible
formatting errors, see the

Details

section of the formatter class specification.
**Throws:** IOError

- If an I/O error occurs.

---

#### readPassword

public char[] readPassword​(

String

fmt,

Object

... args)

Provides a formatted prompt, then reads a password or passphrase from
the console with echoing disabled.

readPassword

```java
public char[] readPassword()
```

Reads a password or passphrase from the console with echoing disabled

**Returns:** A character array containing the password or passphrase read
from the console, not including any line-termination characters,
or

null

if an end of stream has been reached.
**Throws:** IOError

- If an I/O error occurs.

---

#### readPassword

public char[] readPassword()

Reads a password or passphrase from the console with echoing disabled

flush

```java
public void flush()
```

Flushes the console and forces any buffered output to be written
immediately .

**Specified by:** flush

in interface

Flushable

---

#### flush

public void flush()

Flushes the console and forces any buffered output to be written
immediately .

---

