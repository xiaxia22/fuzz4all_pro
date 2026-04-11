# Class ExifGPSTagSet

**Source:** `java.desktop\javax\imageio\plugins\tiff\ExifGPSTagSet.html`

### Class Description

```java
public final class
ExifGPSTagSet

extends
TIFFTagSet
```

A class representing the tags found in an Exif GPS Info IFD.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9
**See Also:** ExifTIFFTagSet

---

### Field Details

#### public static final int TAG_GPS_VERSION_ID

A tag indicating the GPS tag version (type BYTE, count = 4).

**See Also:**
- GPS_VERSION_2_2

,

Constant Field Values

---

#### public static final
String
GPS_VERSION_2_2

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2. The value equals the US-ASCII encoding of the byte array

{'2', '2', '0', '0'}

.

**See Also:**
- TAG_GPS_VERSION_ID

,

Constant Field Values

---

#### public static final int TAG_GPS_LATITUDE_REF

A tag indicating the North or South latitude (type ASCII, count = 2).

**See Also:**
- LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

---

#### public static final int TAG_GPS_LATITUDE

A tag indicating the Latitude (type RATIONAL, count = 3).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_LONGITUDE_REF

A tag indicating the East or West Longitude (type ASCII, count = 2).

**See Also:**
- LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

---

#### public static final int TAG_GPS_LONGITUDE

A tag indicating the Longitude (type RATIONAL, count = 3).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_ALTITUDE_REF

A tag indicating the Altitude reference (type BYTE, count = 1);

**See Also:**
- ALTITUDE_REF_SEA_LEVEL

,

ALTITUDE_REF_SEA_LEVEL_REFERENCE

,

Constant Field Values

---

#### public static final int TAG_GPS_ALTITUDE

A tag indicating the Altitude (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_TIME_STAMP

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_SATELLITES

A tag indicating the GPS satellites used for measurement (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_STATUS

A tag indicating the GPS receiver status (type ASCII, count = 2).

**See Also:**
- STATUS_MEASUREMENT_IN_PROGRESS

,

STATUS_MEASUREMENT_INTEROPERABILITY

,

Constant Field Values

---

#### public static final int TAG_GPS_MEASURE_MODE

A tag indicating the GPS measurement mode (type ASCII, count = 2).

**See Also:**
- MEASURE_MODE_2D

,

MEASURE_MODE_3D

,

Constant Field Values

---

#### public static final int TAG_GPS_DOP

A tag indicating the Measurement precision (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_SPEED_REF

A tag indicating the Speed unit (type ASCII, count = 2).

**See Also:**
- SPEED_REF_KILOMETERS_PER_HOUR

,

SPEED_REF_MILES_PER_HOUR

,

SPEED_REF_KNOTS

,

Constant Field Values

---

#### public static final int TAG_GPS_SPEED

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_TRACK_REF

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

**See Also:**
- DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### public static final int TAG_GPS_TRACK

A tag indicating the Direction of movement (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_IMG_DIRECTION_REF

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

**See Also:**
- DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### public static final int TAG_GPS_IMG_DIRECTION

A tag indicating the Direction of image (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_MAP_DATUM

A tag indicating the Geodetic survey data used (type ASCII).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DEST_LATITUDE_REF

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

**See Also:**
- LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

---

#### public static final int TAG_GPS_DEST_LATITUDE

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DEST_LONGITUDE_REF

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

**See Also:**
- LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

---

#### public static final int TAG_GPS_DEST_LONGITUDE

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DEST_BEARING_REF

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

**See Also:**
- DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### public static final int TAG_GPS_DEST_BEARING

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DEST_DISTANCE_REF

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

**See Also:**
- DEST_DISTANCE_REF_KILOMETERS

,

DEST_DISTANCE_REF_MILES

,

DEST_DISTANCE_REF_KNOTS

,

Constant Field Values

---

#### public static final int TAG_GPS_DEST_DISTANCE

A tag indicating the Distance to destination (type RATIONAL, count = 1).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_PROCESSING_METHOD

A tag indicating the Name of GPS processing method (type UNDEFINED).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_AREA_INFORMATION

A tag indicating the Name of GPS area (type UNDEFINED).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DATE_STAMP

A tag indicating the GPS date (type ASCII, count 11).

**See Also:**
- Constant Field Values

---

#### public static final int TAG_GPS_DIFFERENTIAL

A tag indicating the GPS differential correction (type SHORT,
count = 1).

**See Also:**
- DIFFERENTIAL_CORRECTION_NONE

,

DIFFERENTIAL_CORRECTION_APPLIED

,

Constant Field Values

---

#### public static final
String
LATITUDE_REF_NORTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:**
- TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

---

#### public static final
String
LATITUDE_REF_SOUTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:**
- TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

---

#### public static final
String
LONGITUDE_REF_EAST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:**
- TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

---

#### public static final
String
LONGITUDE_REF_WEST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:**
- TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

---

#### public static final int ALTITUDE_REF_SEA_LEVEL

A value to be used with the "GPSAltitudeRef" tag.

**See Also:**
- TAG_GPS_ALTITUDE_REF

,

Constant Field Values

---

#### public static final int ALTITUDE_REF_SEA_LEVEL_REFERENCE

A value to be used with the "GPSAltitudeRef" tag.

**See Also:**
- TAG_GPS_ALTITUDE_REF

,

Constant Field Values

---

#### public static final
String
STATUS_MEASUREMENT_IN_PROGRESS

A value to be used with the "GPSStatus" tag.

**See Also:**
- TAG_GPS_STATUS

,

Constant Field Values

---

#### public static final
String
STATUS_MEASUREMENT_INTEROPERABILITY

A value to be used with the "GPSStatus" tag.

**See Also:**
- TAG_GPS_STATUS

,

Constant Field Values

---

#### public static final
String
MEASURE_MODE_2D

A value to be used with the "GPSMeasureMode" tag.

**See Also:**
- TAG_GPS_MEASURE_MODE

,

Constant Field Values

---

#### public static final
String
MEASURE_MODE_3D

A value to be used with the "GPSMeasureMode" tag.

**See Also:**
- TAG_GPS_MEASURE_MODE

,

Constant Field Values

---

#### public static final
String
SPEED_REF_KILOMETERS_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

**See Also:**
- TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### public static final
String
SPEED_REF_MILES_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

**See Also:**
- TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### public static final
String
SPEED_REF_KNOTS

A value to be used with the "GPSSpeedRef" tag.

**See Also:**
- TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### public static final
String
DIRECTION_REF_TRUE

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:**
- TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

---

#### public static final
String
DIRECTION_REF_MAGNETIC

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:**
- TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

---

#### public static final
String
DEST_DISTANCE_REF_KILOMETERS

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:**
- TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### public static final
String
DEST_DISTANCE_REF_MILES

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:**
- TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### public static final
String
DEST_DISTANCE_REF_KNOTS

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:**
- TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### public static final int DIFFERENTIAL_CORRECTION_NONE

A value to be used with the "GPSDifferential" tag.

**See Also:**
- TAG_GPS_DIFFERENTIAL

,

Constant Field Values

---

#### public static final int DIFFERENTIAL_CORRECTION_APPLIED

A value to be used with the "GPSDifferential" tag.

**See Also:**
- TAG_GPS_DIFFERENTIAL

,

Constant Field Values

---

### Constructor Details

*No entries found.*

### Method Details

#### public static
ExifGPSTagSet
getInstance()

Returns a shared instance of an

ExifGPSTagSet

.

**Returns:**
- an

ExifGPSTagSet

instance.

---

### Additional Sections

#### Class ExifGPSTagSet

java.lang.Object

- javax.imageio.plugins.tiff.TIFFTagSet
- - javax.imageio.plugins.tiff.ExifGPSTagSet

javax.imageio.plugins.tiff.TIFFTagSet

- javax.imageio.plugins.tiff.ExifGPSTagSet

javax.imageio.plugins.tiff.ExifGPSTagSet

```java
public final class
ExifGPSTagSet

extends
TIFFTagSet
```

A class representing the tags found in an Exif GPS Info IFD.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

**Since:** 9
**See Also:** ExifTIFFTagSet

public final class

ExifGPSTagSet

extends

TIFFTagSet

A class representing the tags found in an Exif GPS Info IFD.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

The definitions of the data types referenced by the field
definitions may be found in the

TIFFTag

class.

=========== FIELD SUMMARY ===========

- Field Summary

Fields

Modifier and Type

Field

Description

static int

ALTITUDE_REF_SEA_LEVEL

A value to be used with the "GPSAltitudeRef" tag.

static int

ALTITUDE_REF_SEA_LEVEL_REFERENCE

A value to be used with the "GPSAltitudeRef" tag.

static

String

DEST_DISTANCE_REF_KILOMETERS

A value to be used with the "GPSDestDistanceRef" tag.

static

String

DEST_DISTANCE_REF_KNOTS

A value to be used with the "GPSDestDistanceRef" tag.

static

String

DEST_DISTANCE_REF_MILES

A value to be used with the "GPSDestDistanceRef" tag.

static int

DIFFERENTIAL_CORRECTION_APPLIED

A value to be used with the "GPSDifferential" tag.

static int

DIFFERENTIAL_CORRECTION_NONE

A value to be used with the "GPSDifferential" tag.

static

String

DIRECTION_REF_MAGNETIC

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

static

String

DIRECTION_REF_TRUE

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

static

String

GPS_VERSION_2_2

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2.

static

String

LATITUDE_REF_NORTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

static

String

LATITUDE_REF_SOUTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

static

String

LONGITUDE_REF_EAST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

static

String

LONGITUDE_REF_WEST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

static

String

MEASURE_MODE_2D

A value to be used with the "GPSMeasureMode" tag.

static

String

MEASURE_MODE_3D

A value to be used with the "GPSMeasureMode" tag.

static

String

SPEED_REF_KILOMETERS_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

static

String

SPEED_REF_KNOTS

A value to be used with the "GPSSpeedRef" tag.

static

String

SPEED_REF_MILES_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

static

String

STATUS_MEASUREMENT_IN_PROGRESS

A value to be used with the "GPSStatus" tag.

static

String

STATUS_MEASUREMENT_INTEROPERABILITY

A value to be used with the "GPSStatus" tag.

static int

TAG_GPS_ALTITUDE

A tag indicating the Altitude (type RATIONAL, count = 1).

static int

TAG_GPS_ALTITUDE_REF

A tag indicating the Altitude reference (type BYTE, count = 1);

static int

TAG_GPS_AREA_INFORMATION

A tag indicating the Name of GPS area (type UNDEFINED).

static int

TAG_GPS_DATE_STAMP

A tag indicating the GPS date (type ASCII, count 11).

static int

TAG_GPS_DEST_BEARING

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

static int

TAG_GPS_DEST_BEARING_REF

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

static int

TAG_GPS_DEST_DISTANCE

A tag indicating the Distance to destination (type RATIONAL, count = 1).

static int

TAG_GPS_DEST_DISTANCE_REF

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

static int

TAG_GPS_DEST_LATITUDE

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

static int

TAG_GPS_DEST_LATITUDE_REF

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

static int

TAG_GPS_DEST_LONGITUDE

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

static int

TAG_GPS_DEST_LONGITUDE_REF

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

static int

TAG_GPS_DIFFERENTIAL

A tag indicating the GPS differential correction (type SHORT,
count = 1).

static int

TAG_GPS_DOP

A tag indicating the Measurement precision (type RATIONAL, count = 1).

static int

TAG_GPS_IMG_DIRECTION

A tag indicating the Direction of image (type RATIONAL, count = 1).

static int

TAG_GPS_IMG_DIRECTION_REF

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

static int

TAG_GPS_LATITUDE

A tag indicating the Latitude (type RATIONAL, count = 3).

static int

TAG_GPS_LATITUDE_REF

A tag indicating the North or South latitude (type ASCII, count = 2).

static int

TAG_GPS_LONGITUDE

A tag indicating the Longitude (type RATIONAL, count = 3).

static int

TAG_GPS_LONGITUDE_REF

A tag indicating the East or West Longitude (type ASCII, count = 2).

static int

TAG_GPS_MAP_DATUM

A tag indicating the Geodetic survey data used (type ASCII).

static int

TAG_GPS_MEASURE_MODE

A tag indicating the GPS measurement mode (type ASCII, count = 2).

static int

TAG_GPS_PROCESSING_METHOD

A tag indicating the Name of GPS processing method (type UNDEFINED).

static int

TAG_GPS_SATELLITES

A tag indicating the GPS satellites used for measurement (type ASCII).

static int

TAG_GPS_SPEED

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

static int

TAG_GPS_SPEED_REF

A tag indicating the Speed unit (type ASCII, count = 2).

static int

TAG_GPS_STATUS

A tag indicating the GPS receiver status (type ASCII, count = 2).

static int

TAG_GPS_TIME_STAMP

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

static int

TAG_GPS_TRACK

A tag indicating the Direction of movement (type RATIONAL, count = 1).

static int

TAG_GPS_TRACK_REF

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

static int

TAG_GPS_VERSION_ID

A tag indicating the GPS tag version (type BYTE, count = 4).

========== METHOD SUMMARY ===========

- Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ExifGPSTagSet

getInstance

()

Returns a shared instance of an

ExifGPSTagSet

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

ALTITUDE_REF_SEA_LEVEL

A value to be used with the "GPSAltitudeRef" tag.

static int

ALTITUDE_REF_SEA_LEVEL_REFERENCE

A value to be used with the "GPSAltitudeRef" tag.

static

String

DEST_DISTANCE_REF_KILOMETERS

A value to be used with the "GPSDestDistanceRef" tag.

static

String

DEST_DISTANCE_REF_KNOTS

A value to be used with the "GPSDestDistanceRef" tag.

static

String

DEST_DISTANCE_REF_MILES

A value to be used with the "GPSDestDistanceRef" tag.

static int

DIFFERENTIAL_CORRECTION_APPLIED

A value to be used with the "GPSDifferential" tag.

static int

DIFFERENTIAL_CORRECTION_NONE

A value to be used with the "GPSDifferential" tag.

static

String

DIRECTION_REF_MAGNETIC

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

static

String

DIRECTION_REF_TRUE

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

static

String

GPS_VERSION_2_2

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2.

static

String

LATITUDE_REF_NORTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

static

String

LATITUDE_REF_SOUTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

static

String

LONGITUDE_REF_EAST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

static

String

LONGITUDE_REF_WEST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

static

String

MEASURE_MODE_2D

A value to be used with the "GPSMeasureMode" tag.

static

String

MEASURE_MODE_3D

A value to be used with the "GPSMeasureMode" tag.

static

String

SPEED_REF_KILOMETERS_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

static

String

SPEED_REF_KNOTS

A value to be used with the "GPSSpeedRef" tag.

static

String

SPEED_REF_MILES_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

static

String

STATUS_MEASUREMENT_IN_PROGRESS

A value to be used with the "GPSStatus" tag.

static

String

STATUS_MEASUREMENT_INTEROPERABILITY

A value to be used with the "GPSStatus" tag.

static int

TAG_GPS_ALTITUDE

A tag indicating the Altitude (type RATIONAL, count = 1).

static int

TAG_GPS_ALTITUDE_REF

A tag indicating the Altitude reference (type BYTE, count = 1);

static int

TAG_GPS_AREA_INFORMATION

A tag indicating the Name of GPS area (type UNDEFINED).

static int

TAG_GPS_DATE_STAMP

A tag indicating the GPS date (type ASCII, count 11).

static int

TAG_GPS_DEST_BEARING

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

static int

TAG_GPS_DEST_BEARING_REF

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

static int

TAG_GPS_DEST_DISTANCE

A tag indicating the Distance to destination (type RATIONAL, count = 1).

static int

TAG_GPS_DEST_DISTANCE_REF

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

static int

TAG_GPS_DEST_LATITUDE

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

static int

TAG_GPS_DEST_LATITUDE_REF

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

static int

TAG_GPS_DEST_LONGITUDE

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

static int

TAG_GPS_DEST_LONGITUDE_REF

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

static int

TAG_GPS_DIFFERENTIAL

A tag indicating the GPS differential correction (type SHORT,
count = 1).

static int

TAG_GPS_DOP

A tag indicating the Measurement precision (type RATIONAL, count = 1).

static int

TAG_GPS_IMG_DIRECTION

A tag indicating the Direction of image (type RATIONAL, count = 1).

static int

TAG_GPS_IMG_DIRECTION_REF

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

static int

TAG_GPS_LATITUDE

A tag indicating the Latitude (type RATIONAL, count = 3).

static int

TAG_GPS_LATITUDE_REF

A tag indicating the North or South latitude (type ASCII, count = 2).

static int

TAG_GPS_LONGITUDE

A tag indicating the Longitude (type RATIONAL, count = 3).

static int

TAG_GPS_LONGITUDE_REF

A tag indicating the East or West Longitude (type ASCII, count = 2).

static int

TAG_GPS_MAP_DATUM

A tag indicating the Geodetic survey data used (type ASCII).

static int

TAG_GPS_MEASURE_MODE

A tag indicating the GPS measurement mode (type ASCII, count = 2).

static int

TAG_GPS_PROCESSING_METHOD

A tag indicating the Name of GPS processing method (type UNDEFINED).

static int

TAG_GPS_SATELLITES

A tag indicating the GPS satellites used for measurement (type ASCII).

static int

TAG_GPS_SPEED

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

static int

TAG_GPS_SPEED_REF

A tag indicating the Speed unit (type ASCII, count = 2).

static int

TAG_GPS_STATUS

A tag indicating the GPS receiver status (type ASCII, count = 2).

static int

TAG_GPS_TIME_STAMP

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

static int

TAG_GPS_TRACK

A tag indicating the Direction of movement (type RATIONAL, count = 1).

static int

TAG_GPS_TRACK_REF

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

static int

TAG_GPS_VERSION_ID

A tag indicating the GPS tag version (type BYTE, count = 4).

---

#### Field Summary

A value to be used with the "GPSAltitudeRef" tag.

A value to be used with the "GPSDestDistanceRef" tag.

A value to be used with the "GPSDifferential" tag.

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2.

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

A value to be used with the "GPSMeasureMode" tag.

A value to be used with the "GPSSpeedRef" tag.

A value to be used with the "GPSStatus" tag.

A tag indicating the Altitude (type RATIONAL, count = 1).

A tag indicating the Altitude reference (type BYTE, count = 1);

A tag indicating the Name of GPS area (type UNDEFINED).

A tag indicating the GPS date (type ASCII, count 11).

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

A tag indicating the Distance to destination (type RATIONAL, count = 1).

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

A tag indicating the GPS differential correction (type SHORT,
count = 1).

A tag indicating the Measurement precision (type RATIONAL, count = 1).

A tag indicating the Direction of image (type RATIONAL, count = 1).

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

A tag indicating the Latitude (type RATIONAL, count = 3).

A tag indicating the North or South latitude (type ASCII, count = 2).

A tag indicating the Longitude (type RATIONAL, count = 3).

A tag indicating the East or West Longitude (type ASCII, count = 2).

A tag indicating the Geodetic survey data used (type ASCII).

A tag indicating the GPS measurement mode (type ASCII, count = 2).

A tag indicating the Name of GPS processing method (type UNDEFINED).

A tag indicating the GPS satellites used for measurement (type ASCII).

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

A tag indicating the Speed unit (type ASCII, count = 2).

A tag indicating the GPS receiver status (type ASCII, count = 2).

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

A tag indicating the Direction of movement (type RATIONAL, count = 1).

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

A tag indicating the GPS tag version (type BYTE, count = 4).

Method Summary

All Methods

Static Methods

Concrete Methods

Modifier and Type

Method

Description

static

ExifGPSTagSet

getInstance

()

Returns a shared instance of an

ExifGPSTagSet

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

Returns a shared instance of an

ExifGPSTagSet

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

- TAG_GPS_VERSION_ID

```java
public static final int TAG_GPS_VERSION_ID
```

A tag indicating the GPS tag version (type BYTE, count = 4).

**See Also:** GPS_VERSION_2_2

,

Constant Field Values

- GPS_VERSION_2_2

```java
public static final
String
GPS_VERSION_2_2
```

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2. The value equals the US-ASCII encoding of the byte array

{'2', '2', '0', '0'}

.

**See Also:** TAG_GPS_VERSION_ID

,

Constant Field Values

- TAG_GPS_LATITUDE_REF

```java
public static final int TAG_GPS_LATITUDE_REF
```

A tag indicating the North or South latitude (type ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

- TAG_GPS_LATITUDE

```java
public static final int TAG_GPS_LATITUDE
```

A tag indicating the Latitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_LONGITUDE_REF

```java
public static final int TAG_GPS_LONGITUDE_REF
```

A tag indicating the East or West Longitude (type ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

- TAG_GPS_LONGITUDE

```java
public static final int TAG_GPS_LONGITUDE
```

A tag indicating the Longitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_ALTITUDE_REF

```java
public static final int TAG_GPS_ALTITUDE_REF
```

A tag indicating the Altitude reference (type BYTE, count = 1);

**See Also:** ALTITUDE_REF_SEA_LEVEL

,

ALTITUDE_REF_SEA_LEVEL_REFERENCE

,

Constant Field Values

- TAG_GPS_ALTITUDE

```java
public static final int TAG_GPS_ALTITUDE
```

A tag indicating the Altitude (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_TIME_STAMP

```java
public static final int TAG_GPS_TIME_STAMP
```

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_SATELLITES

```java
public static final int TAG_GPS_SATELLITES
```

A tag indicating the GPS satellites used for measurement (type ASCII).

**See Also:** Constant Field Values

- TAG_GPS_STATUS

```java
public static final int TAG_GPS_STATUS
```

A tag indicating the GPS receiver status (type ASCII, count = 2).

**See Also:** STATUS_MEASUREMENT_IN_PROGRESS

,

STATUS_MEASUREMENT_INTEROPERABILITY

,

Constant Field Values

- TAG_GPS_MEASURE_MODE

```java
public static final int TAG_GPS_MEASURE_MODE
```

A tag indicating the GPS measurement mode (type ASCII, count = 2).

**See Also:** MEASURE_MODE_2D

,

MEASURE_MODE_3D

,

Constant Field Values

- TAG_GPS_DOP

```java
public static final int TAG_GPS_DOP
```

A tag indicating the Measurement precision (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_SPEED_REF

```java
public static final int TAG_GPS_SPEED_REF
```

A tag indicating the Speed unit (type ASCII, count = 2).

**See Also:** SPEED_REF_KILOMETERS_PER_HOUR

,

SPEED_REF_MILES_PER_HOUR

,

SPEED_REF_KNOTS

,

Constant Field Values

- TAG_GPS_SPEED

```java
public static final int TAG_GPS_SPEED
```

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_TRACK_REF

```java
public static final int TAG_GPS_TRACK_REF
```

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_TRACK

```java
public static final int TAG_GPS_TRACK
```

A tag indicating the Direction of movement (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_IMG_DIRECTION_REF

```java
public static final int TAG_GPS_IMG_DIRECTION_REF
```

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_IMG_DIRECTION

```java
public static final int TAG_GPS_IMG_DIRECTION
```

A tag indicating the Direction of image (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_MAP_DATUM

```java
public static final int TAG_GPS_MAP_DATUM
```

A tag indicating the Geodetic survey data used (type ASCII).

**See Also:** Constant Field Values

- TAG_GPS_DEST_LATITUDE_REF

```java
public static final int TAG_GPS_DEST_LATITUDE_REF
```

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

- TAG_GPS_DEST_LATITUDE

```java
public static final int TAG_GPS_DEST_LATITUDE
```

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_DEST_LONGITUDE_REF

```java
public static final int TAG_GPS_DEST_LONGITUDE_REF
```

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

- TAG_GPS_DEST_LONGITUDE

```java
public static final int TAG_GPS_DEST_LONGITUDE
```

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

**See Also:** Constant Field Values

- TAG_GPS_DEST_BEARING_REF

```java
public static final int TAG_GPS_DEST_BEARING_REF
```

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_DEST_BEARING

```java
public static final int TAG_GPS_DEST_BEARING
```

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_DEST_DISTANCE_REF

```java
public static final int TAG_GPS_DEST_DISTANCE_REF
```

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

**See Also:** DEST_DISTANCE_REF_KILOMETERS

,

DEST_DISTANCE_REF_MILES

,

DEST_DISTANCE_REF_KNOTS

,

Constant Field Values

- TAG_GPS_DEST_DISTANCE

```java
public static final int TAG_GPS_DEST_DISTANCE
```

A tag indicating the Distance to destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_PROCESSING_METHOD

```java
public static final int TAG_GPS_PROCESSING_METHOD
```

A tag indicating the Name of GPS processing method (type UNDEFINED).

**See Also:** Constant Field Values

- TAG_GPS_AREA_INFORMATION

```java
public static final int TAG_GPS_AREA_INFORMATION
```

A tag indicating the Name of GPS area (type UNDEFINED).

**See Also:** Constant Field Values

- TAG_GPS_DATE_STAMP

```java
public static final int TAG_GPS_DATE_STAMP
```

A tag indicating the GPS date (type ASCII, count 11).

**See Also:** Constant Field Values

- TAG_GPS_DIFFERENTIAL

```java
public static final int TAG_GPS_DIFFERENTIAL
```

A tag indicating the GPS differential correction (type SHORT,
count = 1).

**See Also:** DIFFERENTIAL_CORRECTION_NONE

,

DIFFERENTIAL_CORRECTION_APPLIED

,

Constant Field Values

- LATITUDE_REF_NORTH

```java
public static final
String
LATITUDE_REF_NORTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

- LATITUDE_REF_SOUTH

```java
public static final
String
LATITUDE_REF_SOUTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

- LONGITUDE_REF_EAST

```java
public static final
String
LONGITUDE_REF_EAST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

- LONGITUDE_REF_WEST

```java
public static final
String
LONGITUDE_REF_WEST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

- ALTITUDE_REF_SEA_LEVEL

```java
public static final int ALTITUDE_REF_SEA_LEVEL
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

- ALTITUDE_REF_SEA_LEVEL_REFERENCE

```java
public static final int ALTITUDE_REF_SEA_LEVEL_REFERENCE
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

- STATUS_MEASUREMENT_IN_PROGRESS

```java
public static final
String
STATUS_MEASUREMENT_IN_PROGRESS
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

- STATUS_MEASUREMENT_INTEROPERABILITY

```java
public static final
String
STATUS_MEASUREMENT_INTEROPERABILITY
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

- MEASURE_MODE_2D

```java
public static final
String
MEASURE_MODE_2D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

- MEASURE_MODE_3D

```java
public static final
String
MEASURE_MODE_3D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

- SPEED_REF_KILOMETERS_PER_HOUR

```java
public static final
String
SPEED_REF_KILOMETERS_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- SPEED_REF_MILES_PER_HOUR

```java
public static final
String
SPEED_REF_MILES_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- SPEED_REF_KNOTS

```java
public static final
String
SPEED_REF_KNOTS
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- DIRECTION_REF_TRUE

```java
public static final
String
DIRECTION_REF_TRUE
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

- DIRECTION_REF_MAGNETIC

```java
public static final
String
DIRECTION_REF_MAGNETIC
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

- DEST_DISTANCE_REF_KILOMETERS

```java
public static final
String
DEST_DISTANCE_REF_KILOMETERS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DEST_DISTANCE_REF_MILES

```java
public static final
String
DEST_DISTANCE_REF_MILES
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DEST_DISTANCE_REF_KNOTS

```java
public static final
String
DEST_DISTANCE_REF_KNOTS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DIFFERENTIAL_CORRECTION_NONE

```java
public static final int DIFFERENTIAL_CORRECTION_NONE
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

- DIFFERENTIAL_CORRECTION_APPLIED

```java
public static final int DIFFERENTIAL_CORRECTION_APPLIED
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

============ METHOD DETAIL ==========

- Method Detail

- getInstance

```java
public static
ExifGPSTagSet
getInstance()
```

Returns a shared instance of an

ExifGPSTagSet

.

**Returns:** an

ExifGPSTagSet

instance.

Field Detail

- TAG_GPS_VERSION_ID

```java
public static final int TAG_GPS_VERSION_ID
```

A tag indicating the GPS tag version (type BYTE, count = 4).

**See Also:** GPS_VERSION_2_2

,

Constant Field Values

- GPS_VERSION_2_2

```java
public static final
String
GPS_VERSION_2_2
```

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2. The value equals the US-ASCII encoding of the byte array

{'2', '2', '0', '0'}

.

**See Also:** TAG_GPS_VERSION_ID

,

Constant Field Values

- TAG_GPS_LATITUDE_REF

```java
public static final int TAG_GPS_LATITUDE_REF
```

A tag indicating the North or South latitude (type ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

- TAG_GPS_LATITUDE

```java
public static final int TAG_GPS_LATITUDE
```

A tag indicating the Latitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_LONGITUDE_REF

```java
public static final int TAG_GPS_LONGITUDE_REF
```

A tag indicating the East or West Longitude (type ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

- TAG_GPS_LONGITUDE

```java
public static final int TAG_GPS_LONGITUDE
```

A tag indicating the Longitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_ALTITUDE_REF

```java
public static final int TAG_GPS_ALTITUDE_REF
```

A tag indicating the Altitude reference (type BYTE, count = 1);

**See Also:** ALTITUDE_REF_SEA_LEVEL

,

ALTITUDE_REF_SEA_LEVEL_REFERENCE

,

Constant Field Values

- TAG_GPS_ALTITUDE

```java
public static final int TAG_GPS_ALTITUDE
```

A tag indicating the Altitude (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_TIME_STAMP

```java
public static final int TAG_GPS_TIME_STAMP
```

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_SATELLITES

```java
public static final int TAG_GPS_SATELLITES
```

A tag indicating the GPS satellites used for measurement (type ASCII).

**See Also:** Constant Field Values

- TAG_GPS_STATUS

```java
public static final int TAG_GPS_STATUS
```

A tag indicating the GPS receiver status (type ASCII, count = 2).

**See Also:** STATUS_MEASUREMENT_IN_PROGRESS

,

STATUS_MEASUREMENT_INTEROPERABILITY

,

Constant Field Values

- TAG_GPS_MEASURE_MODE

```java
public static final int TAG_GPS_MEASURE_MODE
```

A tag indicating the GPS measurement mode (type ASCII, count = 2).

**See Also:** MEASURE_MODE_2D

,

MEASURE_MODE_3D

,

Constant Field Values

- TAG_GPS_DOP

```java
public static final int TAG_GPS_DOP
```

A tag indicating the Measurement precision (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_SPEED_REF

```java
public static final int TAG_GPS_SPEED_REF
```

A tag indicating the Speed unit (type ASCII, count = 2).

**See Also:** SPEED_REF_KILOMETERS_PER_HOUR

,

SPEED_REF_MILES_PER_HOUR

,

SPEED_REF_KNOTS

,

Constant Field Values

- TAG_GPS_SPEED

```java
public static final int TAG_GPS_SPEED
```

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_TRACK_REF

```java
public static final int TAG_GPS_TRACK_REF
```

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_TRACK

```java
public static final int TAG_GPS_TRACK
```

A tag indicating the Direction of movement (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_IMG_DIRECTION_REF

```java
public static final int TAG_GPS_IMG_DIRECTION_REF
```

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_IMG_DIRECTION

```java
public static final int TAG_GPS_IMG_DIRECTION
```

A tag indicating the Direction of image (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_MAP_DATUM

```java
public static final int TAG_GPS_MAP_DATUM
```

A tag indicating the Geodetic survey data used (type ASCII).

**See Also:** Constant Field Values

- TAG_GPS_DEST_LATITUDE_REF

```java
public static final int TAG_GPS_DEST_LATITUDE_REF
```

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

- TAG_GPS_DEST_LATITUDE

```java
public static final int TAG_GPS_DEST_LATITUDE
```

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

**See Also:** Constant Field Values

- TAG_GPS_DEST_LONGITUDE_REF

```java
public static final int TAG_GPS_DEST_LONGITUDE_REF
```

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

- TAG_GPS_DEST_LONGITUDE

```java
public static final int TAG_GPS_DEST_LONGITUDE
```

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

**See Also:** Constant Field Values

- TAG_GPS_DEST_BEARING_REF

```java
public static final int TAG_GPS_DEST_BEARING_REF
```

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

- TAG_GPS_DEST_BEARING

```java
public static final int TAG_GPS_DEST_BEARING
```

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_DEST_DISTANCE_REF

```java
public static final int TAG_GPS_DEST_DISTANCE_REF
```

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

**See Also:** DEST_DISTANCE_REF_KILOMETERS

,

DEST_DISTANCE_REF_MILES

,

DEST_DISTANCE_REF_KNOTS

,

Constant Field Values

- TAG_GPS_DEST_DISTANCE

```java
public static final int TAG_GPS_DEST_DISTANCE
```

A tag indicating the Distance to destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

- TAG_GPS_PROCESSING_METHOD

```java
public static final int TAG_GPS_PROCESSING_METHOD
```

A tag indicating the Name of GPS processing method (type UNDEFINED).

**See Also:** Constant Field Values

- TAG_GPS_AREA_INFORMATION

```java
public static final int TAG_GPS_AREA_INFORMATION
```

A tag indicating the Name of GPS area (type UNDEFINED).

**See Also:** Constant Field Values

- TAG_GPS_DATE_STAMP

```java
public static final int TAG_GPS_DATE_STAMP
```

A tag indicating the GPS date (type ASCII, count 11).

**See Also:** Constant Field Values

- TAG_GPS_DIFFERENTIAL

```java
public static final int TAG_GPS_DIFFERENTIAL
```

A tag indicating the GPS differential correction (type SHORT,
count = 1).

**See Also:** DIFFERENTIAL_CORRECTION_NONE

,

DIFFERENTIAL_CORRECTION_APPLIED

,

Constant Field Values

- LATITUDE_REF_NORTH

```java
public static final
String
LATITUDE_REF_NORTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

- LATITUDE_REF_SOUTH

```java
public static final
String
LATITUDE_REF_SOUTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

- LONGITUDE_REF_EAST

```java
public static final
String
LONGITUDE_REF_EAST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

- LONGITUDE_REF_WEST

```java
public static final
String
LONGITUDE_REF_WEST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

- ALTITUDE_REF_SEA_LEVEL

```java
public static final int ALTITUDE_REF_SEA_LEVEL
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

- ALTITUDE_REF_SEA_LEVEL_REFERENCE

```java
public static final int ALTITUDE_REF_SEA_LEVEL_REFERENCE
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

- STATUS_MEASUREMENT_IN_PROGRESS

```java
public static final
String
STATUS_MEASUREMENT_IN_PROGRESS
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

- STATUS_MEASUREMENT_INTEROPERABILITY

```java
public static final
String
STATUS_MEASUREMENT_INTEROPERABILITY
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

- MEASURE_MODE_2D

```java
public static final
String
MEASURE_MODE_2D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

- MEASURE_MODE_3D

```java
public static final
String
MEASURE_MODE_3D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

- SPEED_REF_KILOMETERS_PER_HOUR

```java
public static final
String
SPEED_REF_KILOMETERS_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- SPEED_REF_MILES_PER_HOUR

```java
public static final
String
SPEED_REF_MILES_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- SPEED_REF_KNOTS

```java
public static final
String
SPEED_REF_KNOTS
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

- DIRECTION_REF_TRUE

```java
public static final
String
DIRECTION_REF_TRUE
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

- DIRECTION_REF_MAGNETIC

```java
public static final
String
DIRECTION_REF_MAGNETIC
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

- DEST_DISTANCE_REF_KILOMETERS

```java
public static final
String
DEST_DISTANCE_REF_KILOMETERS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DEST_DISTANCE_REF_MILES

```java
public static final
String
DEST_DISTANCE_REF_MILES
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DEST_DISTANCE_REF_KNOTS

```java
public static final
String
DEST_DISTANCE_REF_KNOTS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

- DIFFERENTIAL_CORRECTION_NONE

```java
public static final int DIFFERENTIAL_CORRECTION_NONE
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

- DIFFERENTIAL_CORRECTION_APPLIED

```java
public static final int DIFFERENTIAL_CORRECTION_APPLIED
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

---

#### Field Detail

TAG_GPS_VERSION_ID

```java
public static final int TAG_GPS_VERSION_ID
```

A tag indicating the GPS tag version (type BYTE, count = 4).

**See Also:** GPS_VERSION_2_2

,

Constant Field Values

---

#### TAG_GPS_VERSION_ID

public static final int TAG_GPS_VERSION_ID

A tag indicating the GPS tag version (type BYTE, count = 4).

GPS_VERSION_2_2

```java
public static final
String
GPS_VERSION_2_2
```

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2. The value equals the US-ASCII encoding of the byte array

{'2', '2', '0', '0'}

.

**See Also:** TAG_GPS_VERSION_ID

,

Constant Field Values

---

#### GPS_VERSION_2_2

public static final

String

GPS_VERSION_2_2

A value to be used with the "GPSVersionID" tag to indicate GPS version
2.2. The value equals the US-ASCII encoding of the byte array

{'2', '2', '0', '0'}

.

TAG_GPS_LATITUDE_REF

```java
public static final int TAG_GPS_LATITUDE_REF
```

A tag indicating the North or South latitude (type ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

---

#### TAG_GPS_LATITUDE_REF

public static final int TAG_GPS_LATITUDE_REF

A tag indicating the North or South latitude (type ASCII, count = 2).

TAG_GPS_LATITUDE

```java
public static final int TAG_GPS_LATITUDE
```

A tag indicating the Latitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

---

#### TAG_GPS_LATITUDE

public static final int TAG_GPS_LATITUDE

A tag indicating the Latitude (type RATIONAL, count = 3).

TAG_GPS_LONGITUDE_REF

```java
public static final int TAG_GPS_LONGITUDE_REF
```

A tag indicating the East or West Longitude (type ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

---

#### TAG_GPS_LONGITUDE_REF

public static final int TAG_GPS_LONGITUDE_REF

A tag indicating the East or West Longitude (type ASCII, count = 2).

TAG_GPS_LONGITUDE

```java
public static final int TAG_GPS_LONGITUDE
```

A tag indicating the Longitude (type RATIONAL, count = 3).

**See Also:** Constant Field Values

---

#### TAG_GPS_LONGITUDE

public static final int TAG_GPS_LONGITUDE

A tag indicating the Longitude (type RATIONAL, count = 3).

TAG_GPS_ALTITUDE_REF

```java
public static final int TAG_GPS_ALTITUDE_REF
```

A tag indicating the Altitude reference (type BYTE, count = 1);

**See Also:** ALTITUDE_REF_SEA_LEVEL

,

ALTITUDE_REF_SEA_LEVEL_REFERENCE

,

Constant Field Values

---

#### TAG_GPS_ALTITUDE_REF

public static final int TAG_GPS_ALTITUDE_REF

A tag indicating the Altitude reference (type BYTE, count = 1);

TAG_GPS_ALTITUDE

```java
public static final int TAG_GPS_ALTITUDE
```

A tag indicating the Altitude (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_ALTITUDE

public static final int TAG_GPS_ALTITUDE

A tag indicating the Altitude (type RATIONAL, count = 1).

TAG_GPS_TIME_STAMP

```java
public static final int TAG_GPS_TIME_STAMP
```

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

**See Also:** Constant Field Values

---

#### TAG_GPS_TIME_STAMP

public static final int TAG_GPS_TIME_STAMP

A tag indicating the GPS time (atomic clock) (type RATIONAL, count = 3).

TAG_GPS_SATELLITES

```java
public static final int TAG_GPS_SATELLITES
```

A tag indicating the GPS satellites used for measurement (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_GPS_SATELLITES

public static final int TAG_GPS_SATELLITES

A tag indicating the GPS satellites used for measurement (type ASCII).

TAG_GPS_STATUS

```java
public static final int TAG_GPS_STATUS
```

A tag indicating the GPS receiver status (type ASCII, count = 2).

**See Also:** STATUS_MEASUREMENT_IN_PROGRESS

,

STATUS_MEASUREMENT_INTEROPERABILITY

,

Constant Field Values

---

#### TAG_GPS_STATUS

public static final int TAG_GPS_STATUS

A tag indicating the GPS receiver status (type ASCII, count = 2).

TAG_GPS_MEASURE_MODE

```java
public static final int TAG_GPS_MEASURE_MODE
```

A tag indicating the GPS measurement mode (type ASCII, count = 2).

**See Also:** MEASURE_MODE_2D

,

MEASURE_MODE_3D

,

Constant Field Values

---

#### TAG_GPS_MEASURE_MODE

public static final int TAG_GPS_MEASURE_MODE

A tag indicating the GPS measurement mode (type ASCII, count = 2).

TAG_GPS_DOP

```java
public static final int TAG_GPS_DOP
```

A tag indicating the Measurement precision (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_DOP

public static final int TAG_GPS_DOP

A tag indicating the Measurement precision (type RATIONAL, count = 1).

TAG_GPS_SPEED_REF

```java
public static final int TAG_GPS_SPEED_REF
```

A tag indicating the Speed unit (type ASCII, count = 2).

**See Also:** SPEED_REF_KILOMETERS_PER_HOUR

,

SPEED_REF_MILES_PER_HOUR

,

SPEED_REF_KNOTS

,

Constant Field Values

---

#### TAG_GPS_SPEED_REF

public static final int TAG_GPS_SPEED_REF

A tag indicating the Speed unit (type ASCII, count = 2).

TAG_GPS_SPEED

```java
public static final int TAG_GPS_SPEED
```

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_SPEED

public static final int TAG_GPS_SPEED

A tag indicating the Speed of GPS receiver (type RATIONAL, count = 1).

TAG_GPS_TRACK_REF

```java
public static final int TAG_GPS_TRACK_REF
```

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### TAG_GPS_TRACK_REF

public static final int TAG_GPS_TRACK_REF

A tag indicating the Reference for direction of movement (type ASCII,
count = 2).

TAG_GPS_TRACK

```java
public static final int TAG_GPS_TRACK
```

A tag indicating the Direction of movement (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_TRACK

public static final int TAG_GPS_TRACK

A tag indicating the Direction of movement (type RATIONAL, count = 1).

TAG_GPS_IMG_DIRECTION_REF

```java
public static final int TAG_GPS_IMG_DIRECTION_REF
```

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### TAG_GPS_IMG_DIRECTION_REF

public static final int TAG_GPS_IMG_DIRECTION_REF

A tag indicating the Reference for direction of image (type ASCII,
count = 2).

TAG_GPS_IMG_DIRECTION

```java
public static final int TAG_GPS_IMG_DIRECTION
```

A tag indicating the Direction of image (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_IMG_DIRECTION

public static final int TAG_GPS_IMG_DIRECTION

A tag indicating the Direction of image (type RATIONAL, count = 1).

TAG_GPS_MAP_DATUM

```java
public static final int TAG_GPS_MAP_DATUM
```

A tag indicating the Geodetic survey data used (type ASCII).

**See Also:** Constant Field Values

---

#### TAG_GPS_MAP_DATUM

public static final int TAG_GPS_MAP_DATUM

A tag indicating the Geodetic survey data used (type ASCII).

TAG_GPS_DEST_LATITUDE_REF

```java
public static final int TAG_GPS_DEST_LATITUDE_REF
```

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

**See Also:** LATITUDE_REF_NORTH

,

LATITUDE_REF_SOUTH

,

Constant Field Values

---

#### TAG_GPS_DEST_LATITUDE_REF

public static final int TAG_GPS_DEST_LATITUDE_REF

A tag indicating the Reference for latitude of destination (type
ASCII, count = 2).

TAG_GPS_DEST_LATITUDE

```java
public static final int TAG_GPS_DEST_LATITUDE
```

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

**See Also:** Constant Field Values

---

#### TAG_GPS_DEST_LATITUDE

public static final int TAG_GPS_DEST_LATITUDE

A tag indicating the Latitude of destination (type RATIONAL, count = 3).

TAG_GPS_DEST_LONGITUDE_REF

```java
public static final int TAG_GPS_DEST_LONGITUDE_REF
```

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

**See Also:** LONGITUDE_REF_EAST

,

LONGITUDE_REF_WEST

,

Constant Field Values

---

#### TAG_GPS_DEST_LONGITUDE_REF

public static final int TAG_GPS_DEST_LONGITUDE_REF

A tag indicating the Reference for longitude of destination (type
ASCII, count = 2).

TAG_GPS_DEST_LONGITUDE

```java
public static final int TAG_GPS_DEST_LONGITUDE
```

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

**See Also:** Constant Field Values

---

#### TAG_GPS_DEST_LONGITUDE

public static final int TAG_GPS_DEST_LONGITUDE

A tag indicating the Longitude of destination (type RATIONAL,
count = 3).

TAG_GPS_DEST_BEARING_REF

```java
public static final int TAG_GPS_DEST_BEARING_REF
```

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

**See Also:** DIRECTION_REF_TRUE

,

DIRECTION_REF_MAGNETIC

,

Constant Field Values

---

#### TAG_GPS_DEST_BEARING_REF

public static final int TAG_GPS_DEST_BEARING_REF

A tag indicating the Reference for bearing of destination (type ASCII,
count = 2).

TAG_GPS_DEST_BEARING

```java
public static final int TAG_GPS_DEST_BEARING
```

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_DEST_BEARING

public static final int TAG_GPS_DEST_BEARING

A tag indicating the Bearing of destination (type RATIONAL, count = 1).

TAG_GPS_DEST_DISTANCE_REF

```java
public static final int TAG_GPS_DEST_DISTANCE_REF
```

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

**See Also:** DEST_DISTANCE_REF_KILOMETERS

,

DEST_DISTANCE_REF_MILES

,

DEST_DISTANCE_REF_KNOTS

,

Constant Field Values

---

#### TAG_GPS_DEST_DISTANCE_REF

public static final int TAG_GPS_DEST_DISTANCE_REF

A tag indicating the Reference for distance to destination (type ASCII,
count = 2).

TAG_GPS_DEST_DISTANCE

```java
public static final int TAG_GPS_DEST_DISTANCE
```

A tag indicating the Distance to destination (type RATIONAL, count = 1).

**See Also:** Constant Field Values

---

#### TAG_GPS_DEST_DISTANCE

public static final int TAG_GPS_DEST_DISTANCE

A tag indicating the Distance to destination (type RATIONAL, count = 1).

TAG_GPS_PROCESSING_METHOD

```java
public static final int TAG_GPS_PROCESSING_METHOD
```

A tag indicating the Name of GPS processing method (type UNDEFINED).

**See Also:** Constant Field Values

---

#### TAG_GPS_PROCESSING_METHOD

public static final int TAG_GPS_PROCESSING_METHOD

A tag indicating the Name of GPS processing method (type UNDEFINED).

TAG_GPS_AREA_INFORMATION

```java
public static final int TAG_GPS_AREA_INFORMATION
```

A tag indicating the Name of GPS area (type UNDEFINED).

**See Also:** Constant Field Values

---

#### TAG_GPS_AREA_INFORMATION

public static final int TAG_GPS_AREA_INFORMATION

A tag indicating the Name of GPS area (type UNDEFINED).

TAG_GPS_DATE_STAMP

```java
public static final int TAG_GPS_DATE_STAMP
```

A tag indicating the GPS date (type ASCII, count 11).

**See Also:** Constant Field Values

---

#### TAG_GPS_DATE_STAMP

public static final int TAG_GPS_DATE_STAMP

A tag indicating the GPS date (type ASCII, count 11).

TAG_GPS_DIFFERENTIAL

```java
public static final int TAG_GPS_DIFFERENTIAL
```

A tag indicating the GPS differential correction (type SHORT,
count = 1).

**See Also:** DIFFERENTIAL_CORRECTION_NONE

,

DIFFERENTIAL_CORRECTION_APPLIED

,

Constant Field Values

---

#### TAG_GPS_DIFFERENTIAL

public static final int TAG_GPS_DIFFERENTIAL

A tag indicating the GPS differential correction (type SHORT,
count = 1).

LATITUDE_REF_NORTH

```java
public static final
String
LATITUDE_REF_NORTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

---

#### LATITUDE_REF_NORTH

public static final

String

LATITUDE_REF_NORTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

LATITUDE_REF_SOUTH

```java
public static final
String
LATITUDE_REF_SOUTH
```

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

**See Also:** TAG_GPS_LATITUDE_REF

,

TAG_GPS_DEST_LATITUDE_REF

,

Constant Field Values

---

#### LATITUDE_REF_SOUTH

public static final

String

LATITUDE_REF_SOUTH

A value to be used with the "GPSLatitudeRef" and
"GPSDestLatitudeRef" tags.

LONGITUDE_REF_EAST

```java
public static final
String
LONGITUDE_REF_EAST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

---

#### LONGITUDE_REF_EAST

public static final

String

LONGITUDE_REF_EAST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

LONGITUDE_REF_WEST

```java
public static final
String
LONGITUDE_REF_WEST
```

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

**See Also:** TAG_GPS_LONGITUDE_REF

,

TAG_GPS_DEST_LONGITUDE_REF

,

Constant Field Values

---

#### LONGITUDE_REF_WEST

public static final

String

LONGITUDE_REF_WEST

A value to be used with the "GPSLongitudeRef" and
"GPSDestLongitudeRef" tags.

ALTITUDE_REF_SEA_LEVEL

```java
public static final int ALTITUDE_REF_SEA_LEVEL
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

---

#### ALTITUDE_REF_SEA_LEVEL

public static final int ALTITUDE_REF_SEA_LEVEL

A value to be used with the "GPSAltitudeRef" tag.

ALTITUDE_REF_SEA_LEVEL_REFERENCE

```java
public static final int ALTITUDE_REF_SEA_LEVEL_REFERENCE
```

A value to be used with the "GPSAltitudeRef" tag.

**See Also:** TAG_GPS_ALTITUDE_REF

,

Constant Field Values

---

#### ALTITUDE_REF_SEA_LEVEL_REFERENCE

public static final int ALTITUDE_REF_SEA_LEVEL_REFERENCE

A value to be used with the "GPSAltitudeRef" tag.

STATUS_MEASUREMENT_IN_PROGRESS

```java
public static final
String
STATUS_MEASUREMENT_IN_PROGRESS
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

---

#### STATUS_MEASUREMENT_IN_PROGRESS

public static final

String

STATUS_MEASUREMENT_IN_PROGRESS

A value to be used with the "GPSStatus" tag.

STATUS_MEASUREMENT_INTEROPERABILITY

```java
public static final
String
STATUS_MEASUREMENT_INTEROPERABILITY
```

A value to be used with the "GPSStatus" tag.

**See Also:** TAG_GPS_STATUS

,

Constant Field Values

---

#### STATUS_MEASUREMENT_INTEROPERABILITY

public static final

String

STATUS_MEASUREMENT_INTEROPERABILITY

A value to be used with the "GPSStatus" tag.

MEASURE_MODE_2D

```java
public static final
String
MEASURE_MODE_2D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

---

#### MEASURE_MODE_2D

public static final

String

MEASURE_MODE_2D

A value to be used with the "GPSMeasureMode" tag.

MEASURE_MODE_3D

```java
public static final
String
MEASURE_MODE_3D
```

A value to be used with the "GPSMeasureMode" tag.

**See Also:** TAG_GPS_MEASURE_MODE

,

Constant Field Values

---

#### MEASURE_MODE_3D

public static final

String

MEASURE_MODE_3D

A value to be used with the "GPSMeasureMode" tag.

SPEED_REF_KILOMETERS_PER_HOUR

```java
public static final
String
SPEED_REF_KILOMETERS_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### SPEED_REF_KILOMETERS_PER_HOUR

public static final

String

SPEED_REF_KILOMETERS_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

SPEED_REF_MILES_PER_HOUR

```java
public static final
String
SPEED_REF_MILES_PER_HOUR
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### SPEED_REF_MILES_PER_HOUR

public static final

String

SPEED_REF_MILES_PER_HOUR

A value to be used with the "GPSSpeedRef" tag.

SPEED_REF_KNOTS

```java
public static final
String
SPEED_REF_KNOTS
```

A value to be used with the "GPSSpeedRef" tag.

**See Also:** TAG_GPS_SPEED_REF

,

Constant Field Values

---

#### SPEED_REF_KNOTS

public static final

String

SPEED_REF_KNOTS

A value to be used with the "GPSSpeedRef" tag.

DIRECTION_REF_TRUE

```java
public static final
String
DIRECTION_REF_TRUE
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

---

#### DIRECTION_REF_TRUE

public static final

String

DIRECTION_REF_TRUE

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

DIRECTION_REF_MAGNETIC

```java
public static final
String
DIRECTION_REF_MAGNETIC
```

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

**See Also:** TAG_GPS_TRACK_REF

,

TAG_GPS_IMG_DIRECTION_REF

,

TAG_GPS_DEST_BEARING_REF

,

Constant Field Values

---

#### DIRECTION_REF_MAGNETIC

public static final

String

DIRECTION_REF_MAGNETIC

A value to be used with the "GPSTrackRef", "GPSImgDirectionRef",
and "GPSDestBearingRef" tags.

DEST_DISTANCE_REF_KILOMETERS

```java
public static final
String
DEST_DISTANCE_REF_KILOMETERS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### DEST_DISTANCE_REF_KILOMETERS

public static final

String

DEST_DISTANCE_REF_KILOMETERS

A value to be used with the "GPSDestDistanceRef" tag.

DEST_DISTANCE_REF_MILES

```java
public static final
String
DEST_DISTANCE_REF_MILES
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### DEST_DISTANCE_REF_MILES

public static final

String

DEST_DISTANCE_REF_MILES

A value to be used with the "GPSDestDistanceRef" tag.

DEST_DISTANCE_REF_KNOTS

```java
public static final
String
DEST_DISTANCE_REF_KNOTS
```

A value to be used with the "GPSDestDistanceRef" tag.

**See Also:** TAG_GPS_DEST_DISTANCE_REF

,

Constant Field Values

---

#### DEST_DISTANCE_REF_KNOTS

public static final

String

DEST_DISTANCE_REF_KNOTS

A value to be used with the "GPSDestDistanceRef" tag.

DIFFERENTIAL_CORRECTION_NONE

```java
public static final int DIFFERENTIAL_CORRECTION_NONE
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

---

#### DIFFERENTIAL_CORRECTION_NONE

public static final int DIFFERENTIAL_CORRECTION_NONE

A value to be used with the "GPSDifferential" tag.

DIFFERENTIAL_CORRECTION_APPLIED

```java
public static final int DIFFERENTIAL_CORRECTION_APPLIED
```

A value to be used with the "GPSDifferential" tag.

**See Also:** TAG_GPS_DIFFERENTIAL

,

Constant Field Values

---

#### DIFFERENTIAL_CORRECTION_APPLIED

public static final int DIFFERENTIAL_CORRECTION_APPLIED

A value to be used with the "GPSDifferential" tag.

Method Detail

- getInstance

```java
public static
ExifGPSTagSet
getInstance()
```

Returns a shared instance of an

ExifGPSTagSet

.

**Returns:** an

ExifGPSTagSet

instance.

---

#### Method Detail

getInstance

```java
public static
ExifGPSTagSet
getInstance()
```

Returns a shared instance of an

ExifGPSTagSet

.

**Returns:** an

ExifGPSTagSet

instance.

---

#### getInstance

public static

ExifGPSTagSet

getInstance()

Returns a shared instance of an

ExifGPSTagSet

.

---

