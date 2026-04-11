# Class SecureLookupSupplier

**Source:** `jdk.dynalink\jdk\dynalink\SecureLookupSupplier.html`

### Class Description

```java
public class
SecureLookupSupplier

extends
Object
```

Provides security-checked access to a

MethodHandles.Lookup

object.
See

getLookup()

for details.

**Direct Known Subclasses:** CallSiteDescriptor

---

### Field Details

#### public static final
String
GET_LOOKUP_PERMISSION_NAME

The name of a runtime permission required to successfully invoke the

getLookup()

method.

**See Also:**
- Constant Field Values

---

### Constructor Details

#### public SecureLookupSupplier​(
MethodHandles.Lookup
lookup)

Creates a new secure lookup supplier, securing the passed lookup.

**Parameters:**
- lookup

- the lookup to secure. Can not be null.

**Throws:**
- NullPointerException

- if null is passed.

---

### Method Details

#### public final
MethodHandles.Lookup
getLookup()

Returns the lookup secured by this

SecureLookupSupplier

.

**Returns:**
- the lookup secured by this

SecureLookupSupplier

.

**Throws:**
- SecurityException

- if the secured lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.

---

#### protected final
MethodHandles.Lookup
getLookupPrivileged()

Returns the value of

getLookup()

without a security check. Can
be used by subclasses to access the lookup quickly.

**Returns:**
- same as returned value of

getLookup()

.

---

### Additional Sections

#### Class SecureLookupSupplier

java.lang.Object

- jdk.dynalink.SecureLookupSupplier

jdk.dynalink.SecureLookupSupplier

**Direct Known Subclasses:** CallSiteDescriptor

```java
public class
SecureLookupSupplier

extends
Object
```

Provides security-checked access to a

MethodHandles.Lookup

object.
See

getLookup()

for details.

public class

SecureLookupSupplier

extends

Object

Provides security-checked access to a

MethodHandles.Lookup

object.
See

getLookup()

for details.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static

String

GET_LOOKUP_PERMISSION_NAME

The name of a runtime permission required to successfully invoke the

getLookup()

method.

======== CONSTRUCTOR SUMMARY ========

- Constructor Summary

Constructors

Constructor

Description

SecureLookupSupplier

​(

MethodHandles.Lookup

lookup)

Creates a new secure lookup supplier, securing the passed lookup.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandles.Lookup

getLookup

()

Returns the lookup secured by this

SecureLookupSupplier

.

protected

MethodHandles.Lookup

getLookupPrivileged

()

Returns the value of

getLookup()

without a security check.

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

Field Summary

Fields

Modifier and Type

Field

Description

static

String

GET_LOOKUP_PERMISSION_NAME

The name of a runtime permission required to successfully invoke the

getLookup()

method.

---

#### Field Summary

The name of a runtime permission required to successfully invoke the

getLookup()

method.

Constructor Summary

Constructors

Constructor

Description

SecureLookupSupplier

​(

MethodHandles.Lookup

lookup)

Creates a new secure lookup supplier, securing the passed lookup.

---

#### Constructor Summary

Creates a new secure lookup supplier, securing the passed lookup.

Method Summary

All Methods

Instance Methods

Concrete Methods

Modifier and Type

Method

Description

MethodHandles.Lookup

getLookup

()

Returns the lookup secured by this

SecureLookupSupplier

.

protected

MethodHandles.Lookup

getLookupPrivileged

()

Returns the value of

getLookup()

without a security check.

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

Returns the lookup secured by this

SecureLookupSupplier

.

Returns the value of

getLookup()

without a security check.

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

============ FIELD DETAIL ===========

- Field Detail

- GET_LOOKUP_PERMISSION_NAME

```java
public static final
String
GET_LOOKUP_PERMISSION_NAME
```

The name of a runtime permission required to successfully invoke the

getLookup()

method.

**See Also:** Constant Field Values

========= CONSTRUCTOR DETAIL ========

- Constructor Detail

- SecureLookupSupplier

```java
public SecureLookupSupplier​(
MethodHandles.Lookup
lookup)
```

Creates a new secure lookup supplier, securing the passed lookup.

**Parameters:** lookup

- the lookup to secure. Can not be null.
**Throws:** NullPointerException

- if null is passed.

============ METHOD DETAIL ==========

- Method Detail

- getLookup

```java
public final
MethodHandles.Lookup
getLookup()
```

Returns the lookup secured by this

SecureLookupSupplier

.

**Returns:** the lookup secured by this

SecureLookupSupplier

.
**Throws:** SecurityException

- if the secured lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.

- getLookupPrivileged

```java
protected final
MethodHandles.Lookup
getLookupPrivileged()
```

Returns the value of

getLookup()

without a security check. Can
be used by subclasses to access the lookup quickly.

**Returns:** same as returned value of

getLookup()

.

Field Detail

- GET_LOOKUP_PERMISSION_NAME

```java
public static final
String
GET_LOOKUP_PERMISSION_NAME
```

The name of a runtime permission required to successfully invoke the

getLookup()

method.

**See Also:** Constant Field Values

---

#### Field Detail

GET_LOOKUP_PERMISSION_NAME

```java
public static final
String
GET_LOOKUP_PERMISSION_NAME
```

The name of a runtime permission required to successfully invoke the

getLookup()

method.

**See Also:** Constant Field Values

---

#### GET_LOOKUP_PERMISSION_NAME

public static final

String

GET_LOOKUP_PERMISSION_NAME

The name of a runtime permission required to successfully invoke the

getLookup()

method.

Constructor Detail

- SecureLookupSupplier

```java
public SecureLookupSupplier​(
MethodHandles.Lookup
lookup)
```

Creates a new secure lookup supplier, securing the passed lookup.

**Parameters:** lookup

- the lookup to secure. Can not be null.
**Throws:** NullPointerException

- if null is passed.

---

#### Constructor Detail

SecureLookupSupplier

```java
public SecureLookupSupplier​(
MethodHandles.Lookup
lookup)
```

Creates a new secure lookup supplier, securing the passed lookup.

**Parameters:** lookup

- the lookup to secure. Can not be null.
**Throws:** NullPointerException

- if null is passed.

---

#### SecureLookupSupplier

public SecureLookupSupplier​(

MethodHandles.Lookup

lookup)

Creates a new secure lookup supplier, securing the passed lookup.

Method Detail

- getLookup

```java
public final
MethodHandles.Lookup
getLookup()
```

Returns the lookup secured by this

SecureLookupSupplier

.

**Returns:** the lookup secured by this

SecureLookupSupplier

.
**Throws:** SecurityException

- if the secured lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.

- getLookupPrivileged

```java
protected final
MethodHandles.Lookup
getLookupPrivileged()
```

Returns the value of

getLookup()

without a security check. Can
be used by subclasses to access the lookup quickly.

**Returns:** same as returned value of

getLookup()

.

---

#### Method Detail

getLookup

```java
public final
MethodHandles.Lookup
getLookup()
```

Returns the lookup secured by this

SecureLookupSupplier

.

**Returns:** the lookup secured by this

SecureLookupSupplier

.
**Throws:** SecurityException

- if the secured lookup isn't the

MethodHandles.publicLookup()

, and a security manager is present,
and a check for

RuntimePermission("dynalink.getLookup")

fails.

---

#### getLookup

public final

MethodHandles.Lookup

getLookup()

Returns the lookup secured by this

SecureLookupSupplier

.

getLookupPrivileged

```java
protected final
MethodHandles.Lookup
getLookupPrivileged()
```

Returns the value of

getLookup()

without a security check. Can
be used by subclasses to access the lookup quickly.

**Returns:** same as returned value of

getLookup()

.

---

#### getLookupPrivileged

protected final

MethodHandles.Lookup

getLookupPrivileged()

Returns the value of

getLookup()

without a security check. Can
be used by subclasses to access the lookup quickly.

---

