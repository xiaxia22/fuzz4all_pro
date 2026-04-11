# Interface Refreshable

**Source:** `java.base\javax\security\auth\Refreshable.html`

### Class Description

```java
public interface
Refreshable
```

Objects such as credentials may optionally implement this
interface to provide the capability to refresh itself.
For example, a credential with a particular time-restricted lifespan
may implement this interface to allow callers to refresh the time period
for which it is valid.

**All Known Implementing Classes:** KerberosTicket

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### boolean isCurrent()

Determine if this

Object

is current.

**Returns:**
- true if this

Object

is currently current,
false otherwise.

---

#### void refresh()
throws
RefreshFailedException

Update or extend the validity period for this

Object

.

**Throws:**
- SecurityException

- if the caller does not have permission
to update or extend the validity period for this

Object

.
- RefreshFailedException

- if the refresh attempt failed.

---

### Additional Sections

#### Interface Refreshable

**All Known Implementing Classes:** KerberosTicket

```java
public interface
Refreshable
```

Objects such as credentials may optionally implement this
interface to provide the capability to refresh itself.
For example, a credential with a particular time-restricted lifespan
may implement this interface to allow callers to refresh the time period
for which it is valid.

**Since:** 1.4
**See Also:** Subject

public interface

Refreshable

Objects such as credentials may optionally implement this
interface to provide the capability to refresh itself.
For example, a credential with a particular time-restricted lifespan
may implement this interface to allow callers to refresh the time period
for which it is valid.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isCurrent

()

Determine if this

Object

is current.

void

refresh

()

Update or extend the validity period for this

Object

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

boolean

isCurrent

()

Determine if this

Object

is current.

void

refresh

()

Update or extend the validity period for this

Object

.

---

#### Method Summary

Determine if this

Object

is current.

Update or extend the validity period for this

Object

.

============ METHOD DETAIL ==========

- Method Detail

- isCurrent

```java
boolean isCurrent()
```

Determine if this

Object

is current.

**Returns:** true if this

Object

is currently current,
false otherwise.

- refresh

```java
void refresh()
throws
RefreshFailedException
```

Update or extend the validity period for this

Object

.

**Throws:** SecurityException

- if the caller does not have permission
to update or extend the validity period for this

Object

.
**Throws:** RefreshFailedException

- if the refresh attempt failed.

Method Detail

- isCurrent

```java
boolean isCurrent()
```

Determine if this

Object

is current.

**Returns:** true if this

Object

is currently current,
false otherwise.

- refresh

```java
void refresh()
throws
RefreshFailedException
```

Update or extend the validity period for this

Object

.

**Throws:** SecurityException

- if the caller does not have permission
to update or extend the validity period for this

Object

.
**Throws:** RefreshFailedException

- if the refresh attempt failed.

---

#### Method Detail

isCurrent

```java
boolean isCurrent()
```

Determine if this

Object

is current.

**Returns:** true if this

Object

is currently current,
false otherwise.

---

#### isCurrent

boolean isCurrent()

Determine if this

Object

is current.

refresh

```java
void refresh()
throws
RefreshFailedException
```

Update or extend the validity period for this

Object

.

**Throws:** SecurityException

- if the caller does not have permission
to update or extend the validity period for this

Object

.
**Throws:** RefreshFailedException

- if the refresh attempt failed.

---

#### refresh

void refresh()
throws

RefreshFailedException

Update or extend the validity period for this

Object

.

---

