# Class ClassNotLoadedException

**Source:** `jdk.jdi\com\sun\jdi\ClassNotLoadedException.html`

### Class Description

```java
public class
ClassNotLoadedException

extends
Exception
```

Thrown to indicate that the requested class has
not yet been loaded through the appropriate class loader.

Due to the lazy class linking performed by many VMs, it is
possible for a field or variable to be visible in a program
before the associated class is loaded. Until the class is loaded
all that is available is a signature string. If an attempt is made to
set the value of such a field or variable from JDI, the appropriate
type checking cannot be done because the destination class has not been
loaded. The same is true for the element class of array elements.

It is not advisable to solve this problem by attempting a class load on
the fly in this case. There are two problems in having the debugger load
a class instead of waiting for it to load over the normal course
of events.

- There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

To avoid these potential problems, this exception is thrown.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public ClassNotLoadedException​(
String
className)

*No description found.*

---

#### public ClassNotLoadedException​(
String
className,

String
message)

*No description found.*

---

### Method Details

#### public
String
className()

*No description found.*

---

### Additional Sections

#### Class ClassNotLoadedException

java.lang.Object

- java.lang.Throwable
- - java.lang.Exception
- - com.sun.jdi.ClassNotLoadedException

java.lang.Throwable

- java.lang.Exception
- - com.sun.jdi.ClassNotLoadedException

java.lang.Exception

- com.sun.jdi.ClassNotLoadedException

com.sun.jdi.ClassNotLoadedException

**All Implemented Interfaces:** Serializable

```java
public class
ClassNotLoadedException

extends
Exception
```

Thrown to indicate that the requested class has
not yet been loaded through the appropriate class loader.

Due to the lazy class linking performed by many VMs, it is
possible for a field or variable to be visible in a program
before the associated class is loaded. Until the class is loaded
all that is available is a signature string. If an attempt is made to
set the value of such a field or variable from JDI, the appropriate
type checking cannot be done because the destination class has not been
loaded. The same is true for the element class of array elements.

It is not advisable to solve this problem by attempting a class load on
the fly in this case. There are two problems in having the debugger load
a class instead of waiting for it to load over the normal course
of events.

- There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

To avoid these potential problems, this exception is thrown.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

**Since:** 1.3
**See Also:** Serialized Form

public class

ClassNotLoadedException

extends

Exception

Thrown to indicate that the requested class has
not yet been loaded through the appropriate class loader.

Due to the lazy class linking performed by many VMs, it is
possible for a field or variable to be visible in a program
before the associated class is loaded. Until the class is loaded
all that is available is a signature string. If an attempt is made to
set the value of such a field or variable from JDI, the appropriate
type checking cannot be done because the destination class has not been
loaded. The same is true for the element class of array elements.

It is not advisable to solve this problem by attempting a class load on
the fly in this case. There are two problems in having the debugger load
a class instead of waiting for it to load over the normal course
of events.

- There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

To avoid these potential problems, this exception is thrown.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

Due to the lazy class linking performed by many VMs, it is
possible for a field or variable to be visible in a program
before the associated class is loaded. Until the class is loaded
all that is available is a signature string. If an attempt is made to
set the value of such a field or variable from JDI, the appropriate
type checking cannot be done because the destination class has not been
loaded. The same is true for the element class of array elements.

It is not advisable to solve this problem by attempting a class load on
the fly in this case. There are two problems in having the debugger load
a class instead of waiting for it to load over the normal course
of events.

- There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

To avoid these potential problems, this exception is thrown.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

It is not advisable to solve this problem by attempting a class load on
the fly in this case. There are two problems in having the debugger load
a class instead of waiting for it to load over the normal course
of events.

- There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

To avoid these potential problems, this exception is thrown.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

There can be no guarantee that running the appropriate class
loader won't cause a deadlock in loading the
class. Class loaders can consist of arbitrary
Java™ programming language code and the
class loading methods are usually synchronized. Most of the work
done by a debugger happens when threads are suspended. If another
application thread is suspended within the same class loader,
a deadlock is very possible.

Changing the order in which classes are normally loaded may either mask
or reveal bugs in the application. An unintrusive debugger should strive
to leave unchanged the behavior of the application being debugged.

Note that this exception will be thrown until the class in question
is visible to the class loader of enclosing class. (That is, the
class loader of the enclosing class must be an

initiating

class
loader for the class in question.)
See

The Java™ Virtual Machine Specification

for more details.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

ClassNotLoadedException

​(

String

className)

ClassNotLoadedException

​(

String

className,

String

message)

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

className

()

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

ClassNotLoadedException

​(

String

className)

ClassNotLoadedException

​(

String

className,

String

message)

---

#### Constructor Summary

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

String

className

()

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

- ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className)
```

- ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className,

String
message)
```

============ METHOD DETAIL ==========

- Method Detail

- className

```java
public
String
className()
```

Constructor Detail

- ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className)
```

- ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className,

String
message)
```

---

#### Constructor Detail

ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className)
```

---

#### ClassNotLoadedException

public ClassNotLoadedException​(

String

className)

ClassNotLoadedException

```java
public ClassNotLoadedException​(
String
className,

String
message)
```

---

#### ClassNotLoadedException

public ClassNotLoadedException​(

String

className,

String

message)

Method Detail

- className

```java
public
String
className()
```

---

#### Method Detail

className

```java
public
String
className()
```

---

#### className

public

String

className()

---

