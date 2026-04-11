# Interface OpenType

**Source:** `java.desktop\java\awt\font\OpenType.html`

### Class Description

```java
public interface
OpenType
```

The

OpenType

interface represents OpenType and
TrueType fonts. This interface makes it possible to obtain

sfnt

tables from the font. A particular

Font

object can implement this interface.

For more information on TrueType and OpenType fonts, see the
OpenType specification.
(

http://www.microsoft.com/typography/otspec/

).

---

### Field Details

#### static final int TAG_CMAP

Character to glyph mapping. Table tag "cmap" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_HEAD

Font header. Table tag "head" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_NAME

Naming table. Table tag "name" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GLYF

Glyph data. Table tag "glyf" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_MAXP

Maximum profile. Table tag "maxp" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_PREP

CVT preprogram. Table tag "prep" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_HMTX

Horizontal metrics. Table tag "hmtx" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_KERN

Kerning. Table tag "kern" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_HDMX

Horizontal device metrics. Table tag "hdmx" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_LOCA

Index to location. Table tag "loca" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_POST

PostScript Information. Table tag "post" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_OS2

OS/2 and Windows specific metrics. Table tag "OS/2"
in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_CVT

Control value table. Table tag "cvt "
in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GASP

Grid-fitting and scan conversion procedure. Table tag
"gasp" in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_VDMX

Vertical device metrics. Table tag "VDMX" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_VMTX

Vertical metrics. Table tag "vmtx" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_VHEA

Vertical metrics header. Table tag "vhea" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_HHEA

Horizontal metrics header. Table tag "hhea" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_TYP1

Adobe Type 1 font data. Table tag "typ1" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_BSLN

Baseline table. Table tag "bsln" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GSUB

Glyph substitution. Table tag "GSUB" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_DSIG

Digital signature. Table tag "DSIG" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_FPGM

Font program. Table tag "fpgm" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_FVAR

Font variation. Table tag "fvar" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GVAR

Glyph variation. Table tag "gvar" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_CFF

Compact font format (Type1 font). Table tag
"CFF " in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_MMSD

Multiple master supplementary data. Table tag
"MMSD" in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_MMFX

Multiple master font metrics. Table tag
"MMFX" in the Open Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_BASE

Baseline data. Table tag "BASE" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GDEF

Glyph definition. Table tag "GDEF" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_GPOS

Glyph positioning. Table tag "GPOS" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_JSTF

Justification. Table tag "JSTF" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_EBDT

Embedded bitmap data. Table tag "EBDT" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_EBLC

Embedded bitmap location. Table tag "EBLC" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_EBSC

Embedded bitmap scaling. Table tag "EBSC" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_LTSH

Linear threshold. Table tag "LTSH" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_PCLT

PCL 5 data. Table tag "PCLT" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_ACNT

Accent attachment. Table tag "acnt" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_AVAR

Axis variation. Table tag "avar" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_BDAT

Bitmap data. Table tag "bdat" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_BLOC

Bitmap location. Table tag "bloc" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_CVAR

CVT variation. Table tag "cvar" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_FEAT

Feature name. Table tag "feat" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_FDSC

Font descriptors. Table tag "fdsc" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_FMTX

Font metrics. Table tag "fmtx" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_JUST

Justification. Table tag "just" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_LCAR

Ligature caret. Table tag "lcar" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_MORT

Glyph metamorphosis. Table tag "mort" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_OPBD

Optical bounds. Table tag "opbd" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_PROP

Glyph properties. Table tag "prop" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

#### static final int TAG_TRAK

Tracking. Table tag "trak" in the Open
Type Specification.

**See Also:**
- Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### int getVersion()

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

**Returns:**
- the version of the

OpenType

font.

---

#### byte[] getFontTable​(int sfntTag)

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The

byte

array
returned is a copy of the font data in memory.

**Parameters:**
- sfntTag

- a four-character code as a 32-bit integer

**Returns:**
- a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

---

#### byte[] getFontTable​(
String
strSfntTag)

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The byte array returned is a
copy of the font data in memory.

**Parameters:**
- strSfntTag

- a four-character code as a

String

**Returns:**
- a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

---

#### byte[] getFontTable​(int sfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include
items like

cmap

,

name

and

head

.
The byte array returned is a copy of the font data in
memory.

**Parameters:**
- sfntTag

- a four-character code as a 32-bit integer
- offset

- index of first byte to return from table
- count

- number of bytes to return from table

**Returns:**
- a subset of the table corresponding to

sfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

---

#### byte[] getFontTable​(
String
strSfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include items
like

cmap

,

name

and

head

. The

byte

array returned is a copy of the font
data in memory.

**Parameters:**
- strSfntTag

- a four-character code as a

String
- offset

- index of first byte to return from table
- count

- number of bytes to return from table

**Returns:**
- a subset of the table corresponding to

strSfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

---

#### int getFontTableSize​(int sfntTag)

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:**
- sfntTag

- a four-character code as a 32-bit integer

**Returns:**
- the size of the table corresponding to the specified
tag.

---

#### int getFontTableSize​(
String
strSfntTag)

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:**
- strSfntTag

- a four-character code as a

String

**Returns:**
- the size of the table corresponding to the specified tag.

---

### Additional Sections

#### Interface OpenType

```java
public interface
OpenType
```

The

OpenType

interface represents OpenType and
TrueType fonts. This interface makes it possible to obtain

sfnt

tables from the font. A particular

Font

object can implement this interface.

For more information on TrueType and OpenType fonts, see the
OpenType specification.
(

http://www.microsoft.com/typography/otspec/

).

public interface

OpenType

The

OpenType

interface represents OpenType and
TrueType fonts. This interface makes it possible to obtain

sfnt

tables from the font. A particular

Font

object can implement this interface.

For more information on TrueType and OpenType fonts, see the
OpenType specification.
(

http://www.microsoft.com/typography/otspec/

).

For more information on TrueType and OpenType fonts, see the
OpenType specification.
(

http://www.microsoft.com/typography/otspec/

).

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

TAG_ACNT

Accent attachment.

static int

TAG_AVAR

Axis variation.

static int

TAG_BASE

Baseline data.

static int

TAG_BDAT

Bitmap data.

static int

TAG_BLOC

Bitmap location.

static int

TAG_BSLN

Baseline table.

static int

TAG_CFF

Compact font format (Type1 font).

static int

TAG_CMAP

Character to glyph mapping.

static int

TAG_CVAR

CVT variation.

static int

TAG_CVT

Control value table.

static int

TAG_DSIG

Digital signature.

static int

TAG_EBDT

Embedded bitmap data.

static int

TAG_EBLC

Embedded bitmap location.

static int

TAG_EBSC

Embedded bitmap scaling.

static int

TAG_FDSC

Font descriptors.

static int

TAG_FEAT

Feature name.

static int

TAG_FMTX

Font metrics.

static int

TAG_FPGM

Font program.

static int

TAG_FVAR

Font variation.

static int

TAG_GASP

Grid-fitting and scan conversion procedure.

static int

TAG_GDEF

Glyph definition.

static int

TAG_GLYF

Glyph data.

static int

TAG_GPOS

Glyph positioning.

static int

TAG_GSUB

Glyph substitution.

static int

TAG_GVAR

Glyph variation.

static int

TAG_HDMX

Horizontal device metrics.

static int

TAG_HEAD

Font header.

static int

TAG_HHEA

Horizontal metrics header.

static int

TAG_HMTX

Horizontal metrics.

static int

TAG_JSTF

Justification.

static int

TAG_JUST

Justification.

static int

TAG_KERN

Kerning.

static int

TAG_LCAR

Ligature caret.

static int

TAG_LOCA

Index to location.

static int

TAG_LTSH

Linear threshold.

static int

TAG_MAXP

Maximum profile.

static int

TAG_MMFX

Multiple master font metrics.

static int

TAG_MMSD

Multiple master supplementary data.

static int

TAG_MORT

Glyph metamorphosis.

static int

TAG_NAME

Naming table.

static int

TAG_OPBD

Optical bounds.

static int

TAG_OS2

OS/2 and Windows specific metrics.

static int

TAG_PCLT

PCL 5 data.

static int

TAG_POST

PostScript Information.

static int

TAG_PREP

CVT preprogram.

static int

TAG_PROP

Glyph properties.

static int

TAG_TRAK

Tracking.

static int

TAG_TYP1

Adobe Type 1 font data.

static int

TAG_VDMX

Vertical device metrics.

static int

TAG_VHEA

Vertical metrics header.

static int

TAG_VMTX

Vertical metrics.

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getFontTable

​(int sfntTag)

Returns the table as an array of bytes for a specified tag.

byte[]

getFontTable

​(int sfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag.

byte[]

getFontTable

​(

String

strSfntTag)

Returns the table as an array of bytes for a specified tag.

byte[]

getFontTable

​(

String

strSfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag.

int

getFontTableSize

​(int sfntTag)

Returns the size of the table for a specified tag.

int

getFontTableSize

​(

String

strSfntTag)

Returns the size of the table for a specified tag.

int

getVersion

()

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

Field Summary

Fields

Modifier and Type

Field

Description

static int

TAG_ACNT

Accent attachment.

static int

TAG_AVAR

Axis variation.

static int

TAG_BASE

Baseline data.

static int

TAG_BDAT

Bitmap data.

static int

TAG_BLOC

Bitmap location.

static int

TAG_BSLN

Baseline table.

static int

TAG_CFF

Compact font format (Type1 font).

static int

TAG_CMAP

Character to glyph mapping.

static int

TAG_CVAR

CVT variation.

static int

TAG_CVT

Control value table.

static int

TAG_DSIG

Digital signature.

static int

TAG_EBDT

Embedded bitmap data.

static int

TAG_EBLC

Embedded bitmap location.

static int

TAG_EBSC

Embedded bitmap scaling.

static int

TAG_FDSC

Font descriptors.

static int

TAG_FEAT

Feature name.

static int

TAG_FMTX

Font metrics.

static int

TAG_FPGM

Font program.

static int

TAG_FVAR

Font variation.

static int

TAG_GASP

Grid-fitting and scan conversion procedure.

static int

TAG_GDEF

Glyph definition.

static int

TAG_GLYF

Glyph data.

static int

TAG_GPOS

Glyph positioning.

static int

TAG_GSUB

Glyph substitution.

static int

TAG_GVAR

Glyph variation.

static int

TAG_HDMX

Horizontal device metrics.

static int

TAG_HEAD

Font header.

static int

TAG_HHEA

Horizontal metrics header.

static int

TAG_HMTX

Horizontal metrics.

static int

TAG_JSTF

Justification.

static int

TAG_JUST

Justification.

static int

TAG_KERN

Kerning.

static int

TAG_LCAR

Ligature caret.

static int

TAG_LOCA

Index to location.

static int

TAG_LTSH

Linear threshold.

static int

TAG_MAXP

Maximum profile.

static int

TAG_MMFX

Multiple master font metrics.

static int

TAG_MMSD

Multiple master supplementary data.

static int

TAG_MORT

Glyph metamorphosis.

static int

TAG_NAME

Naming table.

static int

TAG_OPBD

Optical bounds.

static int

TAG_OS2

OS/2 and Windows specific metrics.

static int

TAG_PCLT

PCL 5 data.

static int

TAG_POST

PostScript Information.

static int

TAG_PREP

CVT preprogram.

static int

TAG_PROP

Glyph properties.

static int

TAG_TRAK

Tracking.

static int

TAG_TYP1

Adobe Type 1 font data.

static int

TAG_VDMX

Vertical device metrics.

static int

TAG_VHEA

Vertical metrics header.

static int

TAG_VMTX

Vertical metrics.

---

#### Field Summary

Accent attachment.

Axis variation.

Baseline data.

Bitmap data.

Bitmap location.

Baseline table.

Compact font format (Type1 font).

Character to glyph mapping.

CVT variation.

Control value table.

Digital signature.

Embedded bitmap data.

Embedded bitmap location.

Embedded bitmap scaling.

Font descriptors.

Feature name.

Font metrics.

Font program.

Font variation.

Grid-fitting and scan conversion procedure.

Glyph definition.

Glyph data.

Glyph positioning.

Glyph substitution.

Glyph variation.

Horizontal device metrics.

Font header.

Horizontal metrics header.

Horizontal metrics.

Justification.

Kerning.

Ligature caret.

Index to location.

Linear threshold.

Maximum profile.

Multiple master font metrics.

Multiple master supplementary data.

Glyph metamorphosis.

Naming table.

Optical bounds.

OS/2 and Windows specific metrics.

PCL 5 data.

PostScript Information.

CVT preprogram.

Glyph properties.

Tracking.

Adobe Type 1 font data.

Vertical device metrics.

Vertical metrics header.

Vertical metrics.

Method Summary

All Methods

Instance Methods

Abstract Methods

Modifier and Type

Method

Description

byte[]

getFontTable

​(int sfntTag)

Returns the table as an array of bytes for a specified tag.

byte[]

getFontTable

​(int sfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag.

byte[]

getFontTable

​(

String

strSfntTag)

Returns the table as an array of bytes for a specified tag.

byte[]

getFontTable

​(

String

strSfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag.

int

getFontTableSize

​(int sfntTag)

Returns the size of the table for a specified tag.

int

getFontTableSize

​(

String

strSfntTag)

Returns the size of the table for a specified tag.

int

getVersion

()

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

---

#### Method Summary

Returns the table as an array of bytes for a specified tag.

Returns a subset of the table as an array of bytes
for a specified tag.

Returns the size of the table for a specified tag.

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

============ FIELD DETAIL ===========

- Field Detail

- TAG_CMAP

```java
static final int TAG_CMAP
```

Character to glyph mapping. Table tag "cmap" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HEAD

```java
static final int TAG_HEAD
```

Font header. Table tag "head" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_NAME

```java
static final int TAG_NAME
```

Naming table. Table tag "name" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GLYF

```java
static final int TAG_GLYF
```

Glyph data. Table tag "glyf" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_MAXP

```java
static final int TAG_MAXP
```

Maximum profile. Table tag "maxp" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PREP

```java
static final int TAG_PREP
```

CVT preprogram. Table tag "prep" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HMTX

```java
static final int TAG_HMTX
```

Horizontal metrics. Table tag "hmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_KERN

```java
static final int TAG_KERN
```

Kerning. Table tag "kern" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HDMX

```java
static final int TAG_HDMX
```

Horizontal device metrics. Table tag "hdmx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LOCA

```java
static final int TAG_LOCA
```

Index to location. Table tag "loca" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_POST

```java
static final int TAG_POST
```

PostScript Information. Table tag "post" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_OS2

```java
static final int TAG_OS2
```

OS/2 and Windows specific metrics. Table tag "OS/2"
in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_CVT

```java
static final int TAG_CVT
```

Control value table. Table tag "cvt "
in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_GASP

```java
static final int TAG_GASP
```

Grid-fitting and scan conversion procedure. Table tag
"gasp" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_VDMX

```java
static final int TAG_VDMX
```

Vertical device metrics. Table tag "VDMX" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_VMTX

```java
static final int TAG_VMTX
```

Vertical metrics. Table tag "vmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_VHEA

```java
static final int TAG_VHEA
```

Vertical metrics header. Table tag "vhea" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HHEA

```java
static final int TAG_HHEA
```

Horizontal metrics header. Table tag "hhea" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_TYP1

```java
static final int TAG_TYP1
```

Adobe Type 1 font data. Table tag "typ1" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BSLN

```java
static final int TAG_BSLN
```

Baseline table. Table tag "bsln" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GSUB

```java
static final int TAG_GSUB
```

Glyph substitution. Table tag "GSUB" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_DSIG

```java
static final int TAG_DSIG
```

Digital signature. Table tag "DSIG" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FPGM

```java
static final int TAG_FPGM
```

Font program. Table tag "fpgm" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FVAR

```java
static final int TAG_FVAR
```

Font variation. Table tag "fvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GVAR

```java
static final int TAG_GVAR
```

Glyph variation. Table tag "gvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_CFF

```java
static final int TAG_CFF
```

Compact font format (Type1 font). Table tag
"CFF " in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_MMSD

```java
static final int TAG_MMSD
```

Multiple master supplementary data. Table tag
"MMSD" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_MMFX

```java
static final int TAG_MMFX
```

Multiple master font metrics. Table tag
"MMFX" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_BASE

```java
static final int TAG_BASE
```

Baseline data. Table tag "BASE" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GDEF

```java
static final int TAG_GDEF
```

Glyph definition. Table tag "GDEF" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GPOS

```java
static final int TAG_GPOS
```

Glyph positioning. Table tag "GPOS" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_JSTF

```java
static final int TAG_JSTF
```

Justification. Table tag "JSTF" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBDT

```java
static final int TAG_EBDT
```

Embedded bitmap data. Table tag "EBDT" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBLC

```java
static final int TAG_EBLC
```

Embedded bitmap location. Table tag "EBLC" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBSC

```java
static final int TAG_EBSC
```

Embedded bitmap scaling. Table tag "EBSC" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LTSH

```java
static final int TAG_LTSH
```

Linear threshold. Table tag "LTSH" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PCLT

```java
static final int TAG_PCLT
```

PCL 5 data. Table tag "PCLT" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_ACNT

```java
static final int TAG_ACNT
```

Accent attachment. Table tag "acnt" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_AVAR

```java
static final int TAG_AVAR
```

Axis variation. Table tag "avar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BDAT

```java
static final int TAG_BDAT
```

Bitmap data. Table tag "bdat" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BLOC

```java
static final int TAG_BLOC
```

Bitmap location. Table tag "bloc" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_CVAR

```java
static final int TAG_CVAR
```

CVT variation. Table tag "cvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FEAT

```java
static final int TAG_FEAT
```

Feature name. Table tag "feat" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FDSC

```java
static final int TAG_FDSC
```

Font descriptors. Table tag "fdsc" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FMTX

```java
static final int TAG_FMTX
```

Font metrics. Table tag "fmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_JUST

```java
static final int TAG_JUST
```

Justification. Table tag "just" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LCAR

```java
static final int TAG_LCAR
```

Ligature caret. Table tag "lcar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_MORT

```java
static final int TAG_MORT
```

Glyph metamorphosis. Table tag "mort" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_OPBD

```java
static final int TAG_OPBD
```

Optical bounds. Table tag "opbd" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PROP

```java
static final int TAG_PROP
```

Glyph properties. Table tag "prop" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_TRAK

```java
static final int TAG_TRAK
```

Tracking. Table tag "trak" in the Open
Type Specification.

**See Also:** Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getVersion

```java
int getVersion()
```

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

**Returns:** the version of the

OpenType

font.

- getFontTable

```java
byte[] getFontTable​(int sfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The

byte

array
returned is a copy of the font data in memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

- getFontTable

```java
byte[] getFontTable​(
String
strSfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The byte array returned is a
copy of the font data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

- getFontTable

```java
byte[] getFontTable​(int sfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include
items like

cmap

,

name

and

head

.
The byte array returned is a copy of the font data in
memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

sfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

- getFontTable

```java
byte[] getFontTable​(
String
strSfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include items
like

cmap

,

name

and

head

. The

byte

array returned is a copy of the font
data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

strSfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

- getFontTableSize

```java
int getFontTableSize​(int sfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** the size of the table corresponding to the specified
tag.

- getFontTableSize

```java
int getFontTableSize​(
String
strSfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** the size of the table corresponding to the specified tag.

Field Detail

- TAG_CMAP

```java
static final int TAG_CMAP
```

Character to glyph mapping. Table tag "cmap" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HEAD

```java
static final int TAG_HEAD
```

Font header. Table tag "head" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_NAME

```java
static final int TAG_NAME
```

Naming table. Table tag "name" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GLYF

```java
static final int TAG_GLYF
```

Glyph data. Table tag "glyf" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_MAXP

```java
static final int TAG_MAXP
```

Maximum profile. Table tag "maxp" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PREP

```java
static final int TAG_PREP
```

CVT preprogram. Table tag "prep" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HMTX

```java
static final int TAG_HMTX
```

Horizontal metrics. Table tag "hmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_KERN

```java
static final int TAG_KERN
```

Kerning. Table tag "kern" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HDMX

```java
static final int TAG_HDMX
```

Horizontal device metrics. Table tag "hdmx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LOCA

```java
static final int TAG_LOCA
```

Index to location. Table tag "loca" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_POST

```java
static final int TAG_POST
```

PostScript Information. Table tag "post" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_OS2

```java
static final int TAG_OS2
```

OS/2 and Windows specific metrics. Table tag "OS/2"
in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_CVT

```java
static final int TAG_CVT
```

Control value table. Table tag "cvt "
in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_GASP

```java
static final int TAG_GASP
```

Grid-fitting and scan conversion procedure. Table tag
"gasp" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_VDMX

```java
static final int TAG_VDMX
```

Vertical device metrics. Table tag "VDMX" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_VMTX

```java
static final int TAG_VMTX
```

Vertical metrics. Table tag "vmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_VHEA

```java
static final int TAG_VHEA
```

Vertical metrics header. Table tag "vhea" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_HHEA

```java
static final int TAG_HHEA
```

Horizontal metrics header. Table tag "hhea" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_TYP1

```java
static final int TAG_TYP1
```

Adobe Type 1 font data. Table tag "typ1" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BSLN

```java
static final int TAG_BSLN
```

Baseline table. Table tag "bsln" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GSUB

```java
static final int TAG_GSUB
```

Glyph substitution. Table tag "GSUB" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_DSIG

```java
static final int TAG_DSIG
```

Digital signature. Table tag "DSIG" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FPGM

```java
static final int TAG_FPGM
```

Font program. Table tag "fpgm" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FVAR

```java
static final int TAG_FVAR
```

Font variation. Table tag "fvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GVAR

```java
static final int TAG_GVAR
```

Glyph variation. Table tag "gvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_CFF

```java
static final int TAG_CFF
```

Compact font format (Type1 font). Table tag
"CFF " in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_MMSD

```java
static final int TAG_MMSD
```

Multiple master supplementary data. Table tag
"MMSD" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_MMFX

```java
static final int TAG_MMFX
```

Multiple master font metrics. Table tag
"MMFX" in the Open Type Specification.

**See Also:** Constant Field Values

- TAG_BASE

```java
static final int TAG_BASE
```

Baseline data. Table tag "BASE" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GDEF

```java
static final int TAG_GDEF
```

Glyph definition. Table tag "GDEF" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_GPOS

```java
static final int TAG_GPOS
```

Glyph positioning. Table tag "GPOS" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_JSTF

```java
static final int TAG_JSTF
```

Justification. Table tag "JSTF" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBDT

```java
static final int TAG_EBDT
```

Embedded bitmap data. Table tag "EBDT" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBLC

```java
static final int TAG_EBLC
```

Embedded bitmap location. Table tag "EBLC" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_EBSC

```java
static final int TAG_EBSC
```

Embedded bitmap scaling. Table tag "EBSC" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LTSH

```java
static final int TAG_LTSH
```

Linear threshold. Table tag "LTSH" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PCLT

```java
static final int TAG_PCLT
```

PCL 5 data. Table tag "PCLT" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_ACNT

```java
static final int TAG_ACNT
```

Accent attachment. Table tag "acnt" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_AVAR

```java
static final int TAG_AVAR
```

Axis variation. Table tag "avar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BDAT

```java
static final int TAG_BDAT
```

Bitmap data. Table tag "bdat" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_BLOC

```java
static final int TAG_BLOC
```

Bitmap location. Table tag "bloc" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_CVAR

```java
static final int TAG_CVAR
```

CVT variation. Table tag "cvar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FEAT

```java
static final int TAG_FEAT
```

Feature name. Table tag "feat" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FDSC

```java
static final int TAG_FDSC
```

Font descriptors. Table tag "fdsc" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_FMTX

```java
static final int TAG_FMTX
```

Font metrics. Table tag "fmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_JUST

```java
static final int TAG_JUST
```

Justification. Table tag "just" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_LCAR

```java
static final int TAG_LCAR
```

Ligature caret. Table tag "lcar" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_MORT

```java
static final int TAG_MORT
```

Glyph metamorphosis. Table tag "mort" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_OPBD

```java
static final int TAG_OPBD
```

Optical bounds. Table tag "opbd" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_PROP

```java
static final int TAG_PROP
```

Glyph properties. Table tag "prop" in the Open
Type Specification.

**See Also:** Constant Field Values

- TAG_TRAK

```java
static final int TAG_TRAK
```

Tracking. Table tag "trak" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### Field Detail

TAG_CMAP

```java
static final int TAG_CMAP
```

Character to glyph mapping. Table tag "cmap" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_CMAP

static final int TAG_CMAP

Character to glyph mapping. Table tag "cmap" in the Open
Type Specification.

TAG_HEAD

```java
static final int TAG_HEAD
```

Font header. Table tag "head" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_HEAD

static final int TAG_HEAD

Font header. Table tag "head" in the Open
Type Specification.

TAG_NAME

```java
static final int TAG_NAME
```

Naming table. Table tag "name" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_NAME

static final int TAG_NAME

Naming table. Table tag "name" in the Open
Type Specification.

TAG_GLYF

```java
static final int TAG_GLYF
```

Glyph data. Table tag "glyf" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GLYF

static final int TAG_GLYF

Glyph data. Table tag "glyf" in the Open
Type Specification.

TAG_MAXP

```java
static final int TAG_MAXP
```

Maximum profile. Table tag "maxp" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_MAXP

static final int TAG_MAXP

Maximum profile. Table tag "maxp" in the Open
Type Specification.

TAG_PREP

```java
static final int TAG_PREP
```

CVT preprogram. Table tag "prep" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_PREP

static final int TAG_PREP

CVT preprogram. Table tag "prep" in the Open
Type Specification.

TAG_HMTX

```java
static final int TAG_HMTX
```

Horizontal metrics. Table tag "hmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_HMTX

static final int TAG_HMTX

Horizontal metrics. Table tag "hmtx" in the Open
Type Specification.

TAG_KERN

```java
static final int TAG_KERN
```

Kerning. Table tag "kern" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_KERN

static final int TAG_KERN

Kerning. Table tag "kern" in the Open
Type Specification.

TAG_HDMX

```java
static final int TAG_HDMX
```

Horizontal device metrics. Table tag "hdmx" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_HDMX

static final int TAG_HDMX

Horizontal device metrics. Table tag "hdmx" in the Open
Type Specification.

TAG_LOCA

```java
static final int TAG_LOCA
```

Index to location. Table tag "loca" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_LOCA

static final int TAG_LOCA

Index to location. Table tag "loca" in the Open
Type Specification.

TAG_POST

```java
static final int TAG_POST
```

PostScript Information. Table tag "post" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_POST

static final int TAG_POST

PostScript Information. Table tag "post" in the Open
Type Specification.

TAG_OS2

```java
static final int TAG_OS2
```

OS/2 and Windows specific metrics. Table tag "OS/2"
in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_OS2

static final int TAG_OS2

OS/2 and Windows specific metrics. Table tag "OS/2"
in the Open Type Specification.

TAG_CVT

```java
static final int TAG_CVT
```

Control value table. Table tag "cvt "
in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_CVT

static final int TAG_CVT

Control value table. Table tag "cvt "
in the Open Type Specification.

TAG_GASP

```java
static final int TAG_GASP
```

Grid-fitting and scan conversion procedure. Table tag
"gasp" in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GASP

static final int TAG_GASP

Grid-fitting and scan conversion procedure. Table tag
"gasp" in the Open Type Specification.

TAG_VDMX

```java
static final int TAG_VDMX
```

Vertical device metrics. Table tag "VDMX" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_VDMX

static final int TAG_VDMX

Vertical device metrics. Table tag "VDMX" in the Open
Type Specification.

TAG_VMTX

```java
static final int TAG_VMTX
```

Vertical metrics. Table tag "vmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_VMTX

static final int TAG_VMTX

Vertical metrics. Table tag "vmtx" in the Open
Type Specification.

TAG_VHEA

```java
static final int TAG_VHEA
```

Vertical metrics header. Table tag "vhea" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_VHEA

static final int TAG_VHEA

Vertical metrics header. Table tag "vhea" in the Open
Type Specification.

TAG_HHEA

```java
static final int TAG_HHEA
```

Horizontal metrics header. Table tag "hhea" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_HHEA

static final int TAG_HHEA

Horizontal metrics header. Table tag "hhea" in the Open
Type Specification.

TAG_TYP1

```java
static final int TAG_TYP1
```

Adobe Type 1 font data. Table tag "typ1" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_TYP1

static final int TAG_TYP1

Adobe Type 1 font data. Table tag "typ1" in the Open
Type Specification.

TAG_BSLN

```java
static final int TAG_BSLN
```

Baseline table. Table tag "bsln" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_BSLN

static final int TAG_BSLN

Baseline table. Table tag "bsln" in the Open
Type Specification.

TAG_GSUB

```java
static final int TAG_GSUB
```

Glyph substitution. Table tag "GSUB" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GSUB

static final int TAG_GSUB

Glyph substitution. Table tag "GSUB" in the Open
Type Specification.

TAG_DSIG

```java
static final int TAG_DSIG
```

Digital signature. Table tag "DSIG" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_DSIG

static final int TAG_DSIG

Digital signature. Table tag "DSIG" in the Open
Type Specification.

TAG_FPGM

```java
static final int TAG_FPGM
```

Font program. Table tag "fpgm" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_FPGM

static final int TAG_FPGM

Font program. Table tag "fpgm" in the Open
Type Specification.

TAG_FVAR

```java
static final int TAG_FVAR
```

Font variation. Table tag "fvar" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_FVAR

static final int TAG_FVAR

Font variation. Table tag "fvar" in the Open
Type Specification.

TAG_GVAR

```java
static final int TAG_GVAR
```

Glyph variation. Table tag "gvar" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GVAR

static final int TAG_GVAR

Glyph variation. Table tag "gvar" in the Open
Type Specification.

TAG_CFF

```java
static final int TAG_CFF
```

Compact font format (Type1 font). Table tag
"CFF " in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_CFF

static final int TAG_CFF

Compact font format (Type1 font). Table tag
"CFF " in the Open Type Specification.

TAG_MMSD

```java
static final int TAG_MMSD
```

Multiple master supplementary data. Table tag
"MMSD" in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_MMSD

static final int TAG_MMSD

Multiple master supplementary data. Table tag
"MMSD" in the Open Type Specification.

TAG_MMFX

```java
static final int TAG_MMFX
```

Multiple master font metrics. Table tag
"MMFX" in the Open Type Specification.

**See Also:** Constant Field Values

---

#### TAG_MMFX

static final int TAG_MMFX

Multiple master font metrics. Table tag
"MMFX" in the Open Type Specification.

TAG_BASE

```java
static final int TAG_BASE
```

Baseline data. Table tag "BASE" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_BASE

static final int TAG_BASE

Baseline data. Table tag "BASE" in the Open
Type Specification.

TAG_GDEF

```java
static final int TAG_GDEF
```

Glyph definition. Table tag "GDEF" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GDEF

static final int TAG_GDEF

Glyph definition. Table tag "GDEF" in the Open
Type Specification.

TAG_GPOS

```java
static final int TAG_GPOS
```

Glyph positioning. Table tag "GPOS" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_GPOS

static final int TAG_GPOS

Glyph positioning. Table tag "GPOS" in the Open
Type Specification.

TAG_JSTF

```java
static final int TAG_JSTF
```

Justification. Table tag "JSTF" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_JSTF

static final int TAG_JSTF

Justification. Table tag "JSTF" in the Open
Type Specification.

TAG_EBDT

```java
static final int TAG_EBDT
```

Embedded bitmap data. Table tag "EBDT" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_EBDT

static final int TAG_EBDT

Embedded bitmap data. Table tag "EBDT" in the Open
Type Specification.

TAG_EBLC

```java
static final int TAG_EBLC
```

Embedded bitmap location. Table tag "EBLC" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_EBLC

static final int TAG_EBLC

Embedded bitmap location. Table tag "EBLC" in the Open
Type Specification.

TAG_EBSC

```java
static final int TAG_EBSC
```

Embedded bitmap scaling. Table tag "EBSC" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_EBSC

static final int TAG_EBSC

Embedded bitmap scaling. Table tag "EBSC" in the Open
Type Specification.

TAG_LTSH

```java
static final int TAG_LTSH
```

Linear threshold. Table tag "LTSH" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_LTSH

static final int TAG_LTSH

Linear threshold. Table tag "LTSH" in the Open
Type Specification.

TAG_PCLT

```java
static final int TAG_PCLT
```

PCL 5 data. Table tag "PCLT" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_PCLT

static final int TAG_PCLT

PCL 5 data. Table tag "PCLT" in the Open
Type Specification.

TAG_ACNT

```java
static final int TAG_ACNT
```

Accent attachment. Table tag "acnt" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_ACNT

static final int TAG_ACNT

Accent attachment. Table tag "acnt" in the Open
Type Specification.

TAG_AVAR

```java
static final int TAG_AVAR
```

Axis variation. Table tag "avar" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_AVAR

static final int TAG_AVAR

Axis variation. Table tag "avar" in the Open
Type Specification.

TAG_BDAT

```java
static final int TAG_BDAT
```

Bitmap data. Table tag "bdat" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_BDAT

static final int TAG_BDAT

Bitmap data. Table tag "bdat" in the Open
Type Specification.

TAG_BLOC

```java
static final int TAG_BLOC
```

Bitmap location. Table tag "bloc" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_BLOC

static final int TAG_BLOC

Bitmap location. Table tag "bloc" in the Open
Type Specification.

TAG_CVAR

```java
static final int TAG_CVAR
```

CVT variation. Table tag "cvar" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_CVAR

static final int TAG_CVAR

CVT variation. Table tag "cvar" in the Open
Type Specification.

TAG_FEAT

```java
static final int TAG_FEAT
```

Feature name. Table tag "feat" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_FEAT

static final int TAG_FEAT

Feature name. Table tag "feat" in the Open
Type Specification.

TAG_FDSC

```java
static final int TAG_FDSC
```

Font descriptors. Table tag "fdsc" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_FDSC

static final int TAG_FDSC

Font descriptors. Table tag "fdsc" in the Open
Type Specification.

TAG_FMTX

```java
static final int TAG_FMTX
```

Font metrics. Table tag "fmtx" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_FMTX

static final int TAG_FMTX

Font metrics. Table tag "fmtx" in the Open
Type Specification.

TAG_JUST

```java
static final int TAG_JUST
```

Justification. Table tag "just" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_JUST

static final int TAG_JUST

Justification. Table tag "just" in the Open
Type Specification.

TAG_LCAR

```java
static final int TAG_LCAR
```

Ligature caret. Table tag "lcar" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_LCAR

static final int TAG_LCAR

Ligature caret. Table tag "lcar" in the Open
Type Specification.

TAG_MORT

```java
static final int TAG_MORT
```

Glyph metamorphosis. Table tag "mort" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_MORT

static final int TAG_MORT

Glyph metamorphosis. Table tag "mort" in the Open
Type Specification.

TAG_OPBD

```java
static final int TAG_OPBD
```

Optical bounds. Table tag "opbd" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_OPBD

static final int TAG_OPBD

Optical bounds. Table tag "opbd" in the Open
Type Specification.

TAG_PROP

```java
static final int TAG_PROP
```

Glyph properties. Table tag "prop" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_PROP

static final int TAG_PROP

Glyph properties. Table tag "prop" in the Open
Type Specification.

TAG_TRAK

```java
static final int TAG_TRAK
```

Tracking. Table tag "trak" in the Open
Type Specification.

**See Also:** Constant Field Values

---

#### TAG_TRAK

static final int TAG_TRAK

Tracking. Table tag "trak" in the Open
Type Specification.

Method Detail

- getVersion

```java
int getVersion()
```

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

**Returns:** the version of the

OpenType

font.

- getFontTable

```java
byte[] getFontTable​(int sfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The

byte

array
returned is a copy of the font data in memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

- getFontTable

```java
byte[] getFontTable​(
String
strSfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The byte array returned is a
copy of the font data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

- getFontTable

```java
byte[] getFontTable​(int sfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include
items like

cmap

,

name

and

head

.
The byte array returned is a copy of the font data in
memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

sfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

- getFontTable

```java
byte[] getFontTable​(
String
strSfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include items
like

cmap

,

name

and

head

. The

byte

array returned is a copy of the font
data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

strSfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

- getFontTableSize

```java
int getFontTableSize​(int sfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** the size of the table corresponding to the specified
tag.

- getFontTableSize

```java
int getFontTableSize​(
String
strSfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** the size of the table corresponding to the specified tag.

---

#### Method Detail

getVersion

```java
int getVersion()
```

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

**Returns:** the version of the

OpenType

font.

---

#### getVersion

int getVersion()

Returns the version of the

OpenType

font.
1.0 is represented as 0x00010000.

getFontTable

```java
byte[] getFontTable​(int sfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The

byte

array
returned is a copy of the font data in memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

---

#### getFontTable

byte[] getFontTable​(int sfntTag)

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The

byte

array
returned is a copy of the font data in memory.

getFontTable

```java
byte[] getFontTable​(
String
strSfntTag)
```

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The byte array returned is a
copy of the font data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** a

byte

array that is the table that
contains the font data corresponding to the specified
tag.

---

#### getFontTable

byte[] getFontTable​(

String

strSfntTag)

Returns the table as an array of bytes for a specified tag.
Tags for sfnt tables include items like

cmap

,

name

and

head

. The byte array returned is a
copy of the font data in memory.

getFontTable

```java
byte[] getFontTable​(int sfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include
items like

cmap

,

name

and

head

.
The byte array returned is a copy of the font data in
memory.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

sfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

---

#### getFontTable

byte[] getFontTable​(int sfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include
items like

cmap

,

name

and

head

.
The byte array returned is a copy of the font data in
memory.

getFontTable

```java
byte[] getFontTable​(
String
strSfntTag,
int offset,
int count)
```

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include items
like

cmap

,

name

and

head

. The

byte

array returned is a copy of the font
data in memory.

**Parameters:** strSfntTag

- a four-character code as a

String
**Parameters:** offset

- index of first byte to return from table
**Parameters:** count

- number of bytes to return from table
**Returns:** a subset of the table corresponding to

strSfntTag

and containing the bytes
starting at

offset

byte and including

count

bytes.

---

#### getFontTable

byte[] getFontTable​(

String

strSfntTag,
int offset,
int count)

Returns a subset of the table as an array of bytes
for a specified tag. Tags for sfnt tables include items
like

cmap

,

name

and

head

. The

byte

array returned is a copy of the font
data in memory.

getFontTableSize

```java
int getFontTableSize​(int sfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** sfntTag

- a four-character code as a 32-bit integer
**Returns:** the size of the table corresponding to the specified
tag.

---

#### getFontTableSize

int getFontTableSize​(int sfntTag)

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

getFontTableSize

```java
int getFontTableSize​(
String
strSfntTag)
```

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

**Parameters:** strSfntTag

- a four-character code as a

String
**Returns:** the size of the table corresponding to the specified tag.

---

#### getFontTableSize

int getFontTableSize​(

String

strSfntTag)

Returns the size of the table for a specified tag. Tags for sfnt
tables include items like

cmap

,

name

and

head

.

---

