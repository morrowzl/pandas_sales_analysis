{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "**BIG BIG HINT! Look in the instructions to guide you on this task.**"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Dependencies\n",
    "import pandas as pd\n",
    "import os\n",
    "import csv"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# load CSV\n",
    "file= os.path.join(\"2016-FCC-New-Coders-Survey-Data.csv\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Read with pandas\n",
    "new_coders_df=pd.read_csv(file, encoding='iso-8859-1', low_memory=False)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Inspect all columns\n",
    "new_coders_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Extract only columns 0, 1, 2, 3, 4, 7, 8, 9, 10, 11, 29, 30, 32, 36, 37, 45, 48, 56, 110, 111\n",
    "reduced_coders_df=new_coders_df.iloc[:,[0,1,2,3,4,7,8,9,10,11,29,30,32,36,37,45,48,56,110,111]]\n",
    "reduced_coders_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Change \"0\" to \"No\" and \"1\" to \"Yes\" in response columns\n",
    "reduced_coders_df= reduced_coders_df.replace({0.0:\"No\",1.0:\"Yes\"})\n",
    "reduced_coders_df.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Calculate total number of respondents in survey\n",
    "total_surveyed=len(reduced_coders_df)\n",
    "total_surveyed"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Extract rows corresponding only to people who attended a bootcamp\n",
    "attended_bootcamp=reduced_coders_df.loc[reduced_coders_df[\"AttendedBootcamp\"]==\"Yes\"]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Calculate average age of attendees\n",
    "\n",
    "average_age=attended_bootcamp[\"Age\"].mean()\n",
    "\n",
    "\n",
    "# Calculate how many people attended a bootcamp\n",
    "number_of_attendees=attended_bootcamp[\"AttendedBootcamp\"].count()\n",
    "\n",
    "# Calculate how many attendees hold degrees\n",
    "\n",
    "holds_degree=attended_bootcamp[\"SchoolDegree\"].count()\n",
    "\n",
    "# Count number of attendees who self-identify as male; female; or are of non-binary gender identification\n",
    "total_gender=attended_bootcamp[\"Gender\"].count()\n",
    "male=attended_bootcamp[\"Gender\"].value_counts()['Male']\n",
    "female=attended_bootcamp[\"Gender\"].value_counts()['Female']\n",
    "non_specific= total_gender-male-female\n",
    "\n",
    "# Calculate percentage of respondents who attended a bootcamp\n",
    "\n",
    "attended_bootcamp_percentage=(number_of_attendees/total_surveyed)*100\n",
    "\n",
    "# Calculate percentage of respondents belonging to each gender\n",
    "male_percent=(male/total_surveyed)*100\n",
    "female_percent=(female/total_surveyed)*100\n",
    "non_specific_percent=(non_specific/total_surveyed)*100\n",
    "\n",
    "# Calculate percentage of attendees with a school degree\n",
    "\n",
    "holds_degree_percent=(holds_degree/number_of_attendees)*100\n",
    "\n",
    "# Calculate average post-bootcamp salary\n",
    "avg_salary=attended_bootcamp[\"BootcampPostSalary\"].mean()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Create a new table consolodating above calculations\n",
    "summary_table=attended_bootcamp.DataFrame({\"Total Surveyed\":[total_surveyed],\n",
    "                                           \"Total Bootcamp Attendees\":[number_of_attendees],\n",
    "                                           \"Percent Attended a Bootcamp\":[attended_bootcamp_percentage],\n",
    "                                           \"Average Age\":[average_age],\n",
    "                                           \"% Male\":[male_percent],\n",
    "                                           \"% Female\":[female_percent],\n",
    "                                           \"%Non Gender Specific\":[non_specific_percent],\n",
    "                                           \"% with a degree\":[holds_degree_percent],\n",
    "                                           \"Average Post Bootcamp Salary\":[avg_salary]})\n",
    "\n",
    "summary_table=summary_table[[\"Total Surveyed\", \"Total Bootcamp Attended\", \"Average Age\", \"% Male\", \"% Female\", \"% Non Gender Specific\",\"% with a degree\",\"Average Post Bootcamp Salary\"]]\n",
    "summary_table=summary_table.round(2)\n",
    "summary_table"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Improve formatting before outputting spreadsheet\n",
    "\n",
    "summary_table[\"% Male\"]=summary_table[\"% Male\"].map(\"{0:,.2f}%\".format)\n",
    "summary_table[\"% Female\"]=summary_table[\"% Female\"].map(\"{0:,.2f}%\".format)\n",
    "summary_table[\"Percent Attended a Bootcamp\"] = summary_table[\"Percent Attended a Bootcamp\"].map(\"{0:,.2f}%\".format)\n",
    "summary_table[\"% Non Gender Specific\"] = summary_table[\"% Non Gender Specific\"].map(\"{0:,.2f}%\".format)\n",
    "summary_table[\"% with a degree\"]= summary_table[\"% with a degree\"].map(\"{0:,.2f}%\".format)\n",
    "summary_table[\"Average Post Bootcamp Salary\"]= summary_table[\"Average Post Bootcamp Salary\"].map(\"${0:,0f}\".format)\n",
    "summary_table\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {
    "collapsed": true
   },
   "outputs": [],
   "source": [
    "# Export to Excel\n",
    "\n",
    "summary_table.to_excel(\"bootcamppart1.xlsx\", index=False)"
   ]
  }
 ],
 "metadata": {
  "anaconda-cloud": {},
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.7.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}