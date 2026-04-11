# Class ActivationGroupDesc.CommandEnvironment

**Source:** `java.rmi\java\rmi\activation\ActivationGroupDesc.CommandEnvironment.html`

### Class Description

```java
public static class
ActivationGroupDesc.CommandEnvironment

extends
Object

implements
Serializable
```

Startup options for ActivationGroup implementations.

This class allows overriding default system properties and
specifying implementation-defined options for ActivationGroups.

**All Implemented Interfaces:** Serializable

---

### Field Details

*No entries found.*

### Constructor Details

#### public CommandEnvironment​(
String
cmdpath,

String
[] argv)

Create a CommandEnvironment with all the necessary
information.

**Parameters:**
- cmdpath

- the name of the java executable, including
the full path, or

null

, meaning "use rmid's default".
The named program

must

be able to accept multiple

-Dpropname=value

options (as documented for the
"java" tool)
- argv

- extra options which will be used in creating the
ActivationGroup. Null has the same effect as an empty
list.

**Since:**
- 1.2

---

### Method Details

#### public
String
getCommandPath()

Fetch the configured path-qualified java command name.

**Returns:**
- the configured name, or

null

if configured to
accept the default

**Since:**
- 1.2

---

#### public
String
[] getCommandOptions()

Fetch the configured java command options.

**Returns:**
- An array of the command options which will be passed
to the new child command by rmid.
Note that rmid may add other options before or after these
options, or both.
Never returns

null

.

**Since:**
- 1.2

---

#### public boolean equals​(
Object
obj)

Compares two command environments for content equality.

**Overrides:**
- equals

in class

Object

**Parameters:**
- obj

- the Object to compare with

**Returns:**
- true if these Objects are equal; false otherwise.

**See Also:**
- Hashtable

**Since:**
- 1.2

---

#### public int hashCode()

Return identical values for similar

CommandEnvironment

s.

**Overrides:**
- hashCode

in class

Object

**Returns:**
- an integer

**See Also:**
- Hashtable

---

### Additional Sections

#### Class ActivationGroupDesc.CommandEnvironment

java.lang.Object

- java.rmi.activation.ActivationGroupDesc.CommandEnvironment

java.rmi.activation.ActivationGroupDesc.CommandEnvironment

**All Implemented Interfaces:** Serializable

**Enclosing class:** ActivationGroupDesc

```java
public static class
ActivationGroupDesc.CommandEnvironment

extends
Object

implements
Serializable
```

Startup options for ActivationGroup implementations.

This class allows overriding default system properties and
specifying implementation-defined options for ActivationGroups.

**Since:** 1.2
**See Also:** Serialized Form

public static class

ActivationGroupDesc.CommandEnvironment

extends

Object

implements

Serializable

Startup options for ActivationGroup implementations.

This class allows overriding default system properties and
specifying implementation-defined options for ActivationGroups.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

CommandEnvironment

​(

String

cmdpath,

String

[] argv)

Create a CommandEnvironment with all the necessary
information.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares two command environments for content equality.

String

[]

getCommandOptions

()

Fetch the configured java command options.

String

getCommandPath

()

Fetch the configured path-qualified java command name.

int

hashCode

()

Return identical values for similar

CommandEnvironment

s.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Constructor Summary

Constructors

Constructor

Description

CommandEnvironment

​(

String

cmdpath,

String

[] argv)

Create a CommandEnvironment with all the necessary
information.

---

#### Constructor Summary

Create a CommandEnvironment with all the necessary
information.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

boolean

equals

​(

Object

obj)

Compares two command environments for content equality.

String

[]

getCommandOptions

()

Fetch the configured java command options.

String

getCommandPath

()

Fetch the configured path-qualified java command name.

int

hashCode

()

Return identical values for similar

CommandEnvironment

s.

- Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

Compares two command environments for content equality.

Fetch the configured java command options.

Fetch the configured path-qualified java command name.

Return identical values for similar

CommandEnvironment

s.

Methods declared in class java.lang.

Object

clone

,

finalize

,

getClass

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

- CommandEnvironment

```java
public CommandEnvironment​(
String
cmdpath,

String
[] argv)
```

Create a CommandEnvironment with all the necessary
information.

**Parameters:** cmdpath

- the name of the java executable, including
the full path, or

null

, meaning "use rmid's default".
The named program

must

be able to accept multiple

-Dpropname=value

options (as documented for the
"java" tool)
**Parameters:** argv

- extra options which will be used in creating the
ActivationGroup. Null has the same effect as an empty
list.
**Since:** 1.2

============ METHOD DETAIL ==========

- Method Detail

- getCommandPath

```java
public
String
getCommandPath()
```

Fetch the configured path-qualified java command name.

**Returns:** the configured name, or

null

if configured to
accept the default
**Since:** 1.2

- getCommandOptions

```java
public
String
[] getCommandOptions()
```

Fetch the configured java command options.

**Returns:** An array of the command options which will be passed
to the new child command by rmid.
Note that rmid may add other options before or after these
options, or both.
Never returns

null

.
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two command environments for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

- hashCode

```java
public int hashCode()
```

Return identical values for similar

CommandEnvironment

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

Constructor Detail

- CommandEnvironment

```java
public CommandEnvironment​(
String
cmdpath,

String
[] argv)
```

Create a CommandEnvironment with all the necessary
information.

**Parameters:** cmdpath

- the name of the java executable, including
the full path, or

null

, meaning "use rmid's default".
The named program

must

be able to accept multiple

-Dpropname=value

options (as documented for the
"java" tool)
**Parameters:** argv

- extra options which will be used in creating the
ActivationGroup. Null has the same effect as an empty
list.
**Since:** 1.2

---

#### Constructor Detail

CommandEnvironment

```java
public CommandEnvironment​(
String
cmdpath,

String
[] argv)
```

Create a CommandEnvironment with all the necessary
information.

**Parameters:** cmdpath

- the name of the java executable, including
the full path, or

null

, meaning "use rmid's default".
The named program

must

be able to accept multiple

-Dpropname=value

options (as documented for the
"java" tool)
**Parameters:** argv

- extra options which will be used in creating the
ActivationGroup. Null has the same effect as an empty
list.
**Since:** 1.2

---

#### CommandEnvironment

public CommandEnvironment​(

String

cmdpath,

String

[] argv)

Create a CommandEnvironment with all the necessary
information.

Method Detail

- getCommandPath

```java
public
String
getCommandPath()
```

Fetch the configured path-qualified java command name.

**Returns:** the configured name, or

null

if configured to
accept the default
**Since:** 1.2

- getCommandOptions

```java
public
String
[] getCommandOptions()
```

Fetch the configured java command options.

**Returns:** An array of the command options which will be passed
to the new child command by rmid.
Note that rmid may add other options before or after these
options, or both.
Never returns

null

.
**Since:** 1.2

- equals

```java
public boolean equals​(
Object
obj)
```

Compares two command environments for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

- hashCode

```java
public int hashCode()
```

Return identical values for similar

CommandEnvironment

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### Method Detail

getCommandPath

```java
public
String
getCommandPath()
```

Fetch the configured path-qualified java command name.

**Returns:** the configured name, or

null

if configured to
accept the default
**Since:** 1.2

---

#### getCommandPath

public

String

getCommandPath()

Fetch the configured path-qualified java command name.

getCommandOptions

```java
public
String
[] getCommandOptions()
```

Fetch the configured java command options.

**Returns:** An array of the command options which will be passed
to the new child command by rmid.
Note that rmid may add other options before or after these
options, or both.
Never returns

null

.
**Since:** 1.2

---

#### getCommandOptions

public

String

[] getCommandOptions()

Fetch the configured java command options.

equals

```java
public boolean equals​(
Object
obj)
```

Compares two command environments for content equality.

**Overrides:** equals

in class

Object
**Parameters:** obj

- the Object to compare with
**Returns:** true if these Objects are equal; false otherwise.
**Since:** 1.2
**See Also:** Hashtable

---

#### equals

public boolean equals​(

Object

obj)

Compares two command environments for content equality.

hashCode

```java
public int hashCode()
```

Return identical values for similar

CommandEnvironment

s.

**Overrides:** hashCode

in class

Object
**Returns:** an integer
**See Also:** Hashtable

---

#### hashCode

public int hashCode()

Return identical values for similar

CommandEnvironment

s.

---

