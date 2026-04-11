# Enum VMOption.Origin

**Source:** `jdk.management\com\sun\management\VMOption.Origin.html`

### Class Description

```java
public static enum
VMOption.Origin

extends
Enum
<
VMOption.Origin
>
```

Origin of the value of a VM option. It tells where the
value of a VM option came from.

**All Implemented Interfaces:** Serializable

,

Comparable

<

VMOption.Origin

>

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### public static
VMOption.Origin
[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);
```

**Returns:**
- an array containing the constants of this enum type, in the order they are declared

---

#### public static
VMOption.Origin
valueOf​(
String
name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:**
- name

- the name of the enum constant to be returned.

**Returns:**
- the enum constant with the specified name

**Throws:**
- IllegalArgumentException

- if this enum type has no constant with the specified name
- NullPointerException

- if the argument is null

---

### Additional Sections

#### Enum VMOption.Origin

java.lang.Object

- java.lang.Enum

<

VMOption.Origin

>
- - com.sun.management.VMOption.Origin

java.lang.Enum

<

VMOption.Origin

>

- com.sun.management.VMOption.Origin

com.sun.management.VMOption.Origin

**All Implemented Interfaces:** Serializable

,

Comparable

<

VMOption.Origin

>

**Enclosing class:** VMOption

```java
public static enum
VMOption.Origin

extends
Enum
<
VMOption.Origin
>
```

Origin of the value of a VM option. It tells where the
value of a VM option came from.

**Since:** 1.6

public static enum

VMOption.Origin

extends

Enum

<

VMOption.Origin

>

Origin of the value of a VM option. It tells where the
value of a VM option came from.

=========== ENUM CONSTANT SUMMARY ===========

- Enum Constant Summary

Enum Constants

Enum Constant

Description

ATTACH_ON_DEMAND

The VM option was set using the attach framework.

CONFIG_FILE

The VM option was set via a configuration file.

DEFAULT

The VM option has not been set and its value
is the default value.

ENVIRON_VAR

The VM option was set via an environment variable.

ERGONOMIC

The VM option was set via the VM ergonomic support.

MANAGEMENT

The VM option was set via the management interface after the VM
was started.

OTHER

The VM option was set via some other mechanism.

VM_CREATION

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VMOption.Origin

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

VMOption.Origin

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Enum Constant Summary

Enum Constants

Enum Constant

Description

ATTACH_ON_DEMAND

The VM option was set using the attach framework.

CONFIG_FILE

The VM option was set via a configuration file.

DEFAULT

The VM option has not been set and its value
is the default value.

ENVIRON_VAR

The VM option was set via an environment variable.

ERGONOMIC

The VM option was set via the VM ergonomic support.

MANAGEMENT

The VM option was set via the management interface after the VM
was started.

OTHER

The VM option was set via some other mechanism.

VM_CREATION

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

---

#### Enum Constant Summary

The VM option was set using the attach framework.

The VM option was set via a configuration file.

The VM option has not been set and its value
is the default value.

The VM option was set via an environment variable.

The VM option was set via the VM ergonomic support.

The VM option was set via the management interface after the VM
was started.

The VM option was set via some other mechanism.

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

VMOption.Origin

valueOf

​(

String

name)

Returns the enum constant of this type with the specified name.

static

VMOption.Origin

[]

values

()

Returns an array containing the constants of this enum type, in
the order they are declared.

- Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

- Methods declared in class java.lang.

Object

getClass

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

Returns the enum constant of this type with the specified name.

Returns an array containing the constants of this enum type, in
the order they are declared.

Methods declared in class java.lang.

Enum

clone

,

compareTo

,

equals

,

finalize

,

getDeclaringClass

,

hashCode

,

name

,

ordinal

,

toString

,

valueOf

---

#### Methods declared in class java.lang. Enum

Methods declared in class java.lang.

Object

getClass

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

============ ENUM CONSTANT DETAIL ===========

- Enum Constant Detail

- DEFAULT

```java
public static final
VMOption.Origin
DEFAULT
```

The VM option has not been set and its value
is the default value.

- VM_CREATION

```java
public static final
VMOption.Origin
VM_CREATION
```

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

- ENVIRON_VAR

```java
public static final
VMOption.Origin
ENVIRON_VAR
```

The VM option was set via an environment variable.

- CONFIG_FILE

```java
public static final
VMOption.Origin
CONFIG_FILE
```

The VM option was set via a configuration file.

- MANAGEMENT

```java
public static final
VMOption.Origin
MANAGEMENT
```

The VM option was set via the management interface after the VM
was started.

- ERGONOMIC

```java
public static final
VMOption.Origin
ERGONOMIC
```

The VM option was set via the VM ergonomic support.

- ATTACH_ON_DEMAND

```java
public static final
VMOption.Origin
ATTACH_ON_DEMAND
```

The VM option was set using the attach framework.

**Since:** 9

- OTHER

```java
public static final
VMOption.Origin
OTHER
```

The VM option was set via some other mechanism.

============ METHOD DETAIL ==========

- Method Detail

- values

```java
public static
VMOption.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
VMOption.Origin
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

Enum Constant Detail

- DEFAULT

```java
public static final
VMOption.Origin
DEFAULT
```

The VM option has not been set and its value
is the default value.

- VM_CREATION

```java
public static final
VMOption.Origin
VM_CREATION
```

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

- ENVIRON_VAR

```java
public static final
VMOption.Origin
ENVIRON_VAR
```

The VM option was set via an environment variable.

- CONFIG_FILE

```java
public static final
VMOption.Origin
CONFIG_FILE
```

The VM option was set via a configuration file.

- MANAGEMENT

```java
public static final
VMOption.Origin
MANAGEMENT
```

The VM option was set via the management interface after the VM
was started.

- ERGONOMIC

```java
public static final
VMOption.Origin
ERGONOMIC
```

The VM option was set via the VM ergonomic support.

- ATTACH_ON_DEMAND

```java
public static final
VMOption.Origin
ATTACH_ON_DEMAND
```

The VM option was set using the attach framework.

**Since:** 9

- OTHER

```java
public static final
VMOption.Origin
OTHER
```

The VM option was set via some other mechanism.

---

#### Enum Constant Detail

DEFAULT

```java
public static final
VMOption.Origin
DEFAULT
```

The VM option has not been set and its value
is the default value.

---

#### DEFAULT

public static final

VMOption.Origin

DEFAULT

The VM option has not been set and its value
is the default value.

VM_CREATION

```java
public static final
VMOption.Origin
VM_CREATION
```

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

---

#### VM_CREATION

public static final

VMOption.Origin

VM_CREATION

The VM option was set at VM creation time typically
as a command line argument to the launcher or
an argument passed to the VM created using the
JNI invocation interface.

ENVIRON_VAR

```java
public static final
VMOption.Origin
ENVIRON_VAR
```

The VM option was set via an environment variable.

---

#### ENVIRON_VAR

public static final

VMOption.Origin

ENVIRON_VAR

The VM option was set via an environment variable.

CONFIG_FILE

```java
public static final
VMOption.Origin
CONFIG_FILE
```

The VM option was set via a configuration file.

---

#### CONFIG_FILE

public static final

VMOption.Origin

CONFIG_FILE

The VM option was set via a configuration file.

MANAGEMENT

```java
public static final
VMOption.Origin
MANAGEMENT
```

The VM option was set via the management interface after the VM
was started.

---

#### MANAGEMENT

public static final

VMOption.Origin

MANAGEMENT

The VM option was set via the management interface after the VM
was started.

ERGONOMIC

```java
public static final
VMOption.Origin
ERGONOMIC
```

The VM option was set via the VM ergonomic support.

---

#### ERGONOMIC

public static final

VMOption.Origin

ERGONOMIC

The VM option was set via the VM ergonomic support.

ATTACH_ON_DEMAND

```java
public static final
VMOption.Origin
ATTACH_ON_DEMAND
```

The VM option was set using the attach framework.

**Since:** 9

---

#### ATTACH_ON_DEMAND

public static final

VMOption.Origin

ATTACH_ON_DEMAND

The VM option was set using the attach framework.

OTHER

```java
public static final
VMOption.Origin
OTHER
```

The VM option was set via some other mechanism.

---

#### OTHER

public static final

VMOption.Origin

OTHER

The VM option was set via some other mechanism.

Method Detail

- values

```java
public static
VMOption.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

- valueOf

```java
public static
VMOption.Origin
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### Method Detail

values

```java
public static
VMOption.Origin
[] values()
```

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);
```

**Returns:** an array containing the constants of this enum type, in the order they are declared

---

#### values

public static

VMOption.Origin

[] values()

Returns an array containing the constants of this enum type, in
the order they are declared. This method may be used to iterate
over the constants as follows:

```java
for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);
```

for (VMOption.Origin c : VMOption.Origin.values())
System.out.println(c);

valueOf

```java
public static
VMOption.Origin
valueOf​(
String
name)
```

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

**Parameters:** name

- the name of the enum constant to be returned.
**Returns:** the enum constant with the specified name
**Throws:** IllegalArgumentException

- if this enum type has no constant with the specified name
**Throws:** NullPointerException

- if the argument is null

---

#### valueOf

public static

VMOption.Origin

valueOf​(

String

name)

Returns the enum constant of this type with the specified name.
The string must match

exactly

an identifier used to declare an
enum constant in this type. (Extraneous whitespace characters are
not permitted.)

---

