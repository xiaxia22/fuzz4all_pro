# Interface RegisterableService

**Source:** `java.desktop\javax\imageio\spi\RegisterableService.html`

### Class Description

```java
public interface
RegisterableService
```

An optional interface that may be provided by service provider
objects that will be registered with a

ServiceRegistry

. If this interface is present,
notification of registration and deregistration will be performed.

**All Known Implementing Classes:** IIOServiceProvider

,

ImageInputStreamSpi

,

ImageOutputStreamSpi

,

ImageReaderSpi

,

ImageReaderWriterSpi

,

ImageTranscoderSpi

,

ImageWriterSpi

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void onRegistration​(
ServiceRegistry
registry,

Class
<?> category)

Called when an object implementing this interface is added to
the given

category

of the given

registry

. The object may already be registered
under another category or categories.

**Parameters:**
- registry

- a

ServiceRegistry

where this
object has been registered.
- category

- a

Class

object indicating the
registry category under which this object has been registered.

---

#### void onDeregistration​(
ServiceRegistry
registry,

Class
<?> category)

Called when an object implementing this interface is removed
from the given

category

of the given

registry

. The object may still be registered
under another category or categories.

**Parameters:**
- registry

- a

ServiceRegistry

from which this
object is being (wholly or partially) deregistered.
- category

- a

Class

object indicating the
registry category from which this object is being deregistered.

---

### Additional Sections

#### Interface RegisterableService

**All Known Implementing Classes:** IIOServiceProvider

,

ImageInputStreamSpi

,

ImageOutputStreamSpi

,

ImageReaderSpi

,

ImageReaderWriterSpi

,

ImageTranscoderSpi

,

ImageWriterSpi

```java
public interface
RegisterableService
```

An optional interface that may be provided by service provider
objects that will be registered with a

ServiceRegistry

. If this interface is present,
notification of registration and deregistration will be performed.

**See Also:** ServiceRegistry

public interface

RegisterableService

An optional interface that may be provided by service provider
objects that will be registered with a

ServiceRegistry

. If this interface is present,
notification of registration and deregistration will be performed.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

onDeregistration

​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is removed
from the given

category

of the given

registry

.

void

onRegistration

​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is added to
the given

category

of the given

registry

.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

onDeregistration

​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is removed
from the given

category

of the given

registry

.

void

onRegistration

​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is added to
the given

category

of the given

registry

.

---

#### Method Summary

Called when an object implementing this interface is removed
from the given

category

of the given

registry

.

Called when an object implementing this interface is added to
the given

category

of the given

registry

.

============ METHOD DETAIL ==========

- Method Detail

- onRegistration

```java
void onRegistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is added to
the given

category

of the given

registry

. The object may already be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

where this
object has been registered.
**Parameters:** category

- a

Class

object indicating the
registry category under which this object has been registered.

- onDeregistration

```java
void onDeregistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is removed
from the given

category

of the given

registry

. The object may still be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

from which this
object is being (wholly or partially) deregistered.
**Parameters:** category

- a

Class

object indicating the
registry category from which this object is being deregistered.

Method Detail

- onRegistration

```java
void onRegistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is added to
the given

category

of the given

registry

. The object may already be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

where this
object has been registered.
**Parameters:** category

- a

Class

object indicating the
registry category under which this object has been registered.

- onDeregistration

```java
void onDeregistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is removed
from the given

category

of the given

registry

. The object may still be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

from which this
object is being (wholly or partially) deregistered.
**Parameters:** category

- a

Class

object indicating the
registry category from which this object is being deregistered.

---

#### Method Detail

onRegistration

```java
void onRegistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is added to
the given

category

of the given

registry

. The object may already be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

where this
object has been registered.
**Parameters:** category

- a

Class

object indicating the
registry category under which this object has been registered.

---

#### onRegistration

void onRegistration​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is added to
the given

category

of the given

registry

. The object may already be registered
under another category or categories.

onDeregistration

```java
void onDeregistration​(
ServiceRegistry
registry,

Class
<?> category)
```

Called when an object implementing this interface is removed
from the given

category

of the given

registry

. The object may still be registered
under another category or categories.

**Parameters:** registry

- a

ServiceRegistry

from which this
object is being (wholly or partially) deregistered.
**Parameters:** category

- a

Class

object indicating the
registry category from which this object is being deregistered.

---

#### onDeregistration

void onDeregistration​(

ServiceRegistry

registry,

Class

<?> category)

Called when an object implementing this interface is removed
from the given

category

of the given

registry

. The object may still be registered
under another category or categories.

---

