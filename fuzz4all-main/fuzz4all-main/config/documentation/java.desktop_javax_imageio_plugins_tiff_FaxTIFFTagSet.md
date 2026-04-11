# Class FaxTIFFTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\FaxTIFFTagSet.html`

### Class Description

```java
public final class
FaxTIFFTagSet

extends
TIFFTagSet
```

A class representing the extra tags found in a

TIFF-F

(RFC 2036) file.

**Since:** 9

---

### Field Details

#### public static final int TAG_BAD_FAX_LINES

Tag indicating the number of bad fax lines (type SHORT or LONG).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_CLEAN_FAX_DATA

Tag indicating the number of lines of clean fax data (type
SHORT).

**See Also:**
- CLEAN_FAX_DATA_NO_ERRORS

,

CLEAN_FAX_DATA_ERRORS_CORRECTED

,

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

,

Constant Field Values

---

#### public static final int CLEAN_FAX_DATA_NO_ERRORS

A value to be used with the "CleanFaxData" tag.

**See Also:**
- TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### public static final int CLEAN_FAX_DATA_ERRORS_CORRECTED

A value to be used with the "CleanFaxData" tag.

**See Also:**
- TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### public static final int CLEAN_FAX_DATA_ERRORS_UNCORRECTED

A value to be used with the "CleanFaxData" tag.

**See Also:**
- TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### public static final int TAG_CONSECUTIVE_BAD_LINES

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
FaxTIFFTagSet
getInstance()

Returns a shared instance of a

FaxTIFFTagSet

.

**Returns:**
- a

FaxTIFFTagSet

instance.

---

### Additional Sections

#### Class FaxTIFFTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet
- - javax.imageio.plugins.tiff.FaxTIFFTagSet

javax.imageio.plugins.tiff.TIFFTagSet

- javax.imageio.plugins.tiff.FaxTIFFTagSet

javax.imageio.plugins.tiff.FaxTIFFTagSet

```java
public final class
FaxTIFFTagSet

extends
TIFFTagSet
```

A class representing the extra tags found in a

TIFF-F

(RFC 2036) file.

**Since:** 9

public final class

FaxTIFFTagSet

extends

TIFFTagSet

A class representing the extra tags found in a

TIFF-F

(RFC 2036) file.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

CLEAN_FAX_DATA_ERRORS_CORRECTED

A value to be used with the "CleanFaxData" tag.

static int

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

A value to be used with the "CleanFaxData" tag.

static int

CLEAN_FAX_DATA_NO_ERRORS

A value to be used with the "CleanFaxData" tag.

static int

TAG_BAD_FAX_LINES

Tag indicating the number of bad fax lines (type SHORT or LONG).

static int

TAG_CLEAN_FAX_DATA

Tag indicating the number of lines of clean fax data (type
SHORT).

static int

TAG_CONSECUTIVE_BAD_LINES

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FaxTIFFTagSet

getInstance

()

Returns a shared instance of a

FaxTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

static int

CLEAN_FAX_DATA_ERRORS_CORRECTED

A value to be used with the "CleanFaxData" tag.

static int

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

A value to be used with the "CleanFaxData" tag.

static int

CLEAN_FAX_DATA_NO_ERRORS

A value to be used with the "CleanFaxData" tag.

static int

TAG_BAD_FAX_LINES

Tag indicating the number of bad fax lines (type SHORT or LONG).

static int

TAG_CLEAN_FAX_DATA

Tag indicating the number of lines of clean fax data (type
SHORT).

static int

TAG_CONSECUTIVE_BAD_LINES

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

---

#### Field Summary

A value to be used with the "CleanFaxData" tag.

Tag indicating the number of bad fax lines (type SHORT or LONG).

Tag indicating the number of lines of clean fax data (type
SHORT).

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

FaxTIFFTagSet

getInstance

()

Returns a shared instance of a

FaxTIFFTagSet

.

- Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

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

Returns a shared instance of a

FaxTIFFTagSet

.

Methods declared in class javax.imageio.plugins.tiff.

TIFFTagSet

getTag

,

getTag

,

getTagNames

,

getTagNumbers

---

#### Methods declared in class javax.imageio.plugins.tiff. TIFFTagSet

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

- TAG_BAD_FAX_LINES

```java
public static final int TAG_BAD_FAX_LINES
```

Tag indicating the number of bad fax lines (type SHORT or LONG).

**See Also:** Constant Field Values

- TAG_CLEAN_FAX_DATA

```java
public static final int TAG_CLEAN_FAX_DATA
```

Tag indicating the number of lines of clean fax data (type
SHORT).

**See Also:** CLEAN_FAX_DATA_NO_ERRORS

,

CLEAN_FAX_DATA_ERRORS_CORRECTED

,

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

,

Constant Field Values

- CLEAN_FAX_DATA_NO_ERRORS

```java
public static final int CLEAN_FAX_DATA_NO_ERRORS
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- CLEAN_FAX_DATA_ERRORS_CORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_CORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- CLEAN_FAX_DATA_ERRORS_UNCORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_UNCORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- TAG_CONSECUTIVE_BAD_LINES

```java
public static final int TAG_CONSECUTIVE_BAD_LINES
```

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
FaxTIFFTagSet
getInstance()
```

Returns a shared instance of a

FaxTIFFTagSet

.

**Returns:** a

FaxTIFFTagSet

instance.

Field Detail

- TAG_BAD_FAX_LINES

```java
public static final int TAG_BAD_FAX_LINES
```

Tag indicating the number of bad fax lines (type SHORT or LONG).

**See Also:** Constant Field Values

- TAG_CLEAN_FAX_DATA

```java
public static final int TAG_CLEAN_FAX_DATA
```

Tag indicating the number of lines of clean fax data (type
SHORT).

**See Also:** CLEAN_FAX_DATA_NO_ERRORS

,

CLEAN_FAX_DATA_ERRORS_CORRECTED

,

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

,

Constant Field Values

- CLEAN_FAX_DATA_NO_ERRORS

```java
public static final int CLEAN_FAX_DATA_NO_ERRORS
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- CLEAN_FAX_DATA_ERRORS_CORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_CORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- CLEAN_FAX_DATA_ERRORS_UNCORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_UNCORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

- TAG_CONSECUTIVE_BAD_LINES

```java
public static final int TAG_CONSECUTIVE_BAD_LINES
```

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

**See Also:** Constant Field Values

---

#### Field Detail

TAG_BAD_FAX_LINES

```java
public static final int TAG_BAD_FAX_LINES
```

Tag indicating the number of bad fax lines (type SHORT or LONG).

**See Also:** Constant Field Values

---

#### TAG_BAD_FAX_LINES

public static final int TAG_BAD_FAX_LINES

Tag indicating the number of bad fax lines (type SHORT or LONG).

TAG_CLEAN_FAX_DATA

```java
public static final int TAG_CLEAN_FAX_DATA
```

Tag indicating the number of lines of clean fax data (type
SHORT).

**See Also:** CLEAN_FAX_DATA_NO_ERRORS

,

CLEAN_FAX_DATA_ERRORS_CORRECTED

,

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

,

Constant Field Values

---

#### TAG_CLEAN_FAX_DATA

public static final int TAG_CLEAN_FAX_DATA

Tag indicating the number of lines of clean fax data (type
SHORT).

CLEAN_FAX_DATA_NO_ERRORS

```java
public static final int CLEAN_FAX_DATA_NO_ERRORS
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### CLEAN_FAX_DATA_NO_ERRORS

public static final int CLEAN_FAX_DATA_NO_ERRORS

A value to be used with the "CleanFaxData" tag.

CLEAN_FAX_DATA_ERRORS_CORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_CORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### CLEAN_FAX_DATA_ERRORS_CORRECTED

public static final int CLEAN_FAX_DATA_ERRORS_CORRECTED

A value to be used with the "CleanFaxData" tag.

CLEAN_FAX_DATA_ERRORS_UNCORRECTED

```java
public static final int CLEAN_FAX_DATA_ERRORS_UNCORRECTED
```

A value to be used with the "CleanFaxData" tag.

**See Also:** TAG_CLEAN_FAX_DATA

,

Constant Field Values

---

#### CLEAN_FAX_DATA_ERRORS_UNCORRECTED

public static final int CLEAN_FAX_DATA_ERRORS_UNCORRECTED

A value to be used with the "CleanFaxData" tag.

TAG_CONSECUTIVE_BAD_LINES

```java
public static final int TAG_CONSECUTIVE_BAD_LINES
```

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

**See Also:** Constant Field Values

---

#### TAG_CONSECUTIVE_BAD_LINES

public static final int TAG_CONSECUTIVE_BAD_LINES

Tag indicating the number of consecutive bad lines (type
SHORT or LONG).

Method Detail

- getInstance

```java
public static
FaxTIFFTagSet
getInstance()
```

Returns a shared instance of a

FaxTIFFTagSet

.

**Returns:** a

FaxTIFFTagSet

instance.

---

#### Method Detail

getInstance

```java
public static
FaxTIFFTagSet
getInstance()
```

Returns a shared instance of a

FaxTIFFTagSet

.

**Returns:** a

FaxTIFFTagSet

instance.

---

#### getInstance

public static

FaxTIFFTagSet

getInstance()

Returns a shared instance of a

FaxTIFFTagSet

.

---

