# Interface IIOReadWarningListener

**Source:** `java.desktop\javax\imageio\event\IIOReadWarningListener.html`

### Class Description

```java
public interface
IIOReadWarningListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOReadWarningListener

as it is registered
with an

ImageReader

. It is up to the

ImageReader

to provide localized messages.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void warningOccurred​(
ImageReader
source,

String
warning)

Reports the occurrence of a non-fatal error in decoding. Decoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:**
- source

- the

ImageReader

object calling this method.
- warning

- a

String

containing the warning.

---

### Additional Sections

#### Interface IIOReadWarningListener

**All Superinterfaces:** EventListener

```java
public interface
IIOReadWarningListener

extends
EventListener
```

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOReadWarningListener

as it is registered
with an

ImageReader

. It is up to the

ImageReader

to provide localized messages.

**See Also:** ImageReader.addIIOReadWarningListener(javax.imageio.event.IIOReadWarningListener)

,

ImageReader.removeIIOReadWarningListener(javax.imageio.event.IIOReadWarningListener)

public interface

IIOReadWarningListener

extends

EventListener

An interface used by

ImageReader

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOReadWarningListener

as it is registered
with an

ImageReader

. It is up to the

ImageReader

to provide localized messages.

Localization is handled by associating a

Locale

with each

IIOReadWarningListener

as it is registered
with an

ImageReader

. It is up to the

ImageReader

to provide localized messages.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

warningOccurred

​(

ImageReader

source,

String

warning)

Reports the occurrence of a non-fatal error in decoding.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

void

warningOccurred

​(

ImageReader

source,

String

warning)

Reports the occurrence of a non-fatal error in decoding.

---

#### Method Summary

Reports the occurrence of a non-fatal error in decoding.

============ METHOD DETAIL ==========

- Method Detail

- warningOccurred

```java
void warningOccurred​(
ImageReader
source,

String
warning)
```

Reports the occurrence of a non-fatal error in decoding. Decoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** warning

- a

String

containing the warning.

Method Detail

- warningOccurred

```java
void warningOccurred​(
ImageReader
source,

String
warning)
```

Reports the occurrence of a non-fatal error in decoding. Decoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** warning

- a

String

containing the warning.

---

#### Method Detail

warningOccurred

```java
void warningOccurred​(
ImageReader
source,

String
warning)
```

Reports the occurrence of a non-fatal error in decoding. Decoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageReader

object calling this method.
**Parameters:** warning

- a

String

containing the warning.

---

#### warningOccurred

void warningOccurred​(

ImageReader

source,

String

warning)

Reports the occurrence of a non-fatal error in decoding. Decoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

---

