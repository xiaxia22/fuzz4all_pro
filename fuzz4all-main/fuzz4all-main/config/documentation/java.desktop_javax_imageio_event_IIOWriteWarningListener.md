# Interface IIOWriteWarningListener

**Source:** `java.desktop\javax\imageio\event\IIOWriteWarningListener.html`

### Class Description

```java
public interface
IIOWriteWarningListener

extends
EventListener
```

An interface used by

ImageWriter

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOWriteWarningListener

as it is registered
with an

ImageWriter

. It is up to the

ImageWriter

to provide localized messages.

**All Superinterfaces:** EventListener

---

### Field Details

*No entries found.*

### Constructor Details

*No entries found.*

### Method Details

#### void warningOccurred​(
ImageWriter
source,
int imageIndex,

String
warning)

Reports the occurrence of a non-fatal error in encoding. Encoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:**
- source

- the

ImageWriter

object calling this method.
- imageIndex

- the index, starting with 0, of the image
generating the warning.
- warning

- a

String

containing the warning.

---

### Additional Sections

#### Interface IIOWriteWarningListener

**All Superinterfaces:** EventListener

```java
public interface
IIOWriteWarningListener

extends
EventListener
```

An interface used by

ImageWriter

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOWriteWarningListener

as it is registered
with an

ImageWriter

. It is up to the

ImageWriter

to provide localized messages.

**See Also:** ImageWriter.addIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

,

ImageWriter.removeIIOWriteWarningListener(javax.imageio.event.IIOWriteWarningListener)

public interface

IIOWriteWarningListener

extends

EventListener

An interface used by

ImageWriter

implementations to
notify callers of their image and thumbnail reading methods of
warnings (non-fatal errors). Fatal errors cause the relevant
read method to throw an

IIOException

.

Localization is handled by associating a

Locale

with each

IIOWriteWarningListener

as it is registered
with an

ImageWriter

. It is up to the

ImageWriter

to provide localized messages.

Localization is handled by associating a

Locale

with each

IIOWriteWarningListener

as it is registered
with an

ImageWriter

. It is up to the

ImageWriter

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

ImageWriter

source,
int imageIndex,

String

warning)

Reports the occurrence of a non-fatal error in encoding.

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

ImageWriter

source,
int imageIndex,

String

warning)

Reports the occurrence of a non-fatal error in encoding.

---

#### Method Summary

Reports the occurrence of a non-fatal error in encoding.

============ METHOD DETAIL ==========

- Method Detail

- warningOccurred

```java
void warningOccurred​(
ImageWriter
source,
int imageIndex,

String
warning)
```

Reports the occurrence of a non-fatal error in encoding. Encoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** imageIndex

- the index, starting with 0, of the image
generating the warning.
**Parameters:** warning

- a

String

containing the warning.

Method Detail

- warningOccurred

```java
void warningOccurred​(
ImageWriter
source,
int imageIndex,

String
warning)
```

Reports the occurrence of a non-fatal error in encoding. Encoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** imageIndex

- the index, starting with 0, of the image
generating the warning.
**Parameters:** warning

- a

String

containing the warning.

---

#### Method Detail

warningOccurred

```java
void warningOccurred​(
ImageWriter
source,
int imageIndex,

String
warning)
```

Reports the occurrence of a non-fatal error in encoding. Encoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

**Parameters:** source

- the

ImageWriter

object calling this method.
**Parameters:** imageIndex

- the index, starting with 0, of the image
generating the warning.
**Parameters:** warning

- a

String

containing the warning.

---

#### warningOccurred

void warningOccurred​(

ImageWriter

source,
int imageIndex,

String

warning)

Reports the occurrence of a non-fatal error in encoding. Encoding
will continue following the call to this method. The application
may choose to display a dialog, print the warning to the console,
ignore the warning, or take any other action it chooses.

---

