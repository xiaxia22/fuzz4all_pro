# Interface LoaderDelegate

**Source:** `jdk.jshell\jdk\jshell\execution\LoaderDelegate.html`

### Class Description

```java
public interface
LoaderDelegate
```

This interface specifies the loading specific subset of

ExecutionControl

. For use in encapsulating the

ClassLoader

implementation.

**Since:** 9

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException

Attempts to load new classes.

**Parameters:**
- cbcs

- the class name and bytecodes to load

**Throws:**
- ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
- ExecutionControl.NotImplementedException

- if not implemented
- ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)

Notify that classes have been redefined.

**Parameters:**
- cbcs

- the class names and bytecodes that have been redefined

---

#### void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException

Adds the path to the execution class path.

**Parameters:**
- path

- the path to add

**Throws:**
- ExecutionControl.EngineTerminationException

- the execution engine has terminated
- ExecutionControl.InternalException

- an internal problem occurred

---

#### Class
<?> findClass​(
String
name)
throws
ClassNotFoundException

Finds the class with the specified binary name.

**Parameters:**
- name

- the binary name of the class

**Returns:**
- the Class Object

**Throws:**
- ClassNotFoundException

- if the class could not be found

---

### Additional Sections

#### Interface LoaderDelegate

```java
public interface
LoaderDelegate
```

This interface specifies the loading specific subset of

ExecutionControl

. For use in encapsulating the

ClassLoader

implementation.

**Since:** 9

public interface

LoaderDelegate

This interface specifies the loading specific subset of

ExecutionControl

. For use in encapsulating the

ClassLoader

implementation.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

Adds the path to the execution class path.

void

classesRedefined

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Notify that classes have been redefined.

Class

<?>

findClass

​(

String

name)

Finds the class with the specified binary name.

void

load

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to load new classes.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

addToClasspath

​(

String

path)

Adds the path to the execution class path.

void

classesRedefined

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Notify that classes have been redefined.

Class

<?>

findClass

​(

String

name)

Finds the class with the specified binary name.

void

load

​(

ExecutionControl.ClassBytecodes

[] cbcs)

Attempts to load new classes.

---

#### Method Summary

Adds the path to the execution class path.

Notify that classes have been redefined.

Finds the class with the specified binary name.

Attempts to load new classes.

============ METHOD DETAIL ==========

- Method Detail

- load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- classesRedefined

```java
void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class names and bytecodes that have been redefined

- addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- findClass

```java
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

Method Detail

- load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

- classesRedefined

```java
void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class names and bytecodes that have been redefined

- addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

- findClass

```java
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

---

#### Method Detail

load

```java
void load​(
ExecutionControl.ClassBytecodes
[] cbcs)
throws
ExecutionControl.ClassInstallException
,

ExecutionControl.NotImplementedException
,

ExecutionControl.EngineTerminationException
```

Attempts to load new classes.

**Parameters:** cbcs

- the class name and bytecodes to load
**Throws:** ExecutionControl.ClassInstallException

- exception occurred loading the classes,
some or all were not loaded
**Throws:** ExecutionControl.NotImplementedException

- if not implemented
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated

---

#### load

void load​(

ExecutionControl.ClassBytecodes

[] cbcs)
throws

ExecutionControl.ClassInstallException

,

ExecutionControl.NotImplementedException

,

ExecutionControl.EngineTerminationException

Attempts to load new classes.

classesRedefined

```java
void classesRedefined​(
ExecutionControl.ClassBytecodes
[] cbcs)
```

Notify that classes have been redefined.

**Parameters:** cbcs

- the class names and bytecodes that have been redefined

---

#### classesRedefined

void classesRedefined​(

ExecutionControl.ClassBytecodes

[] cbcs)

Notify that classes have been redefined.

addToClasspath

```java
void addToClasspath​(
String
path)
throws
ExecutionControl.EngineTerminationException
,

ExecutionControl.InternalException
```

Adds the path to the execution class path.

**Parameters:** path

- the path to add
**Throws:** ExecutionControl.EngineTerminationException

- the execution engine has terminated
**Throws:** ExecutionControl.InternalException

- an internal problem occurred

---

#### addToClasspath

void addToClasspath​(

String

path)
throws

ExecutionControl.EngineTerminationException

,

ExecutionControl.InternalException

Adds the path to the execution class path.

findClass

```java
Class
<?> findClass​(
String
name)
throws
ClassNotFoundException
```

Finds the class with the specified binary name.

**Parameters:** name

- the binary name of the class
**Returns:** the Class Object
**Throws:** ClassNotFoundException

- if the class could not be found

---

#### findClass

Class

<?> findClass​(

String

name)
throws

ClassNotFoundException

Finds the class with the specified binary name.

---

