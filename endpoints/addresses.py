BATTLEFY_TOURNAMENT_ADDRESS_FORMAT: str = 'https://battlefy.com/{org_name}//{tournament_id}/participants'
"""
The participants address format. 

First param is the tournament organisation name (e.g. inkling-performance-labs),
Second param is the tournament id (e.g. 5fbb02b0a2fd346547539ad9),
Returning e.g. https://battlefy.com/inkling-performance-labs//5fbb02b0a2fd346547539ad9/participants
"""

STAGE_INFO_FETCH_ADDRESS_FORMAT: str = \
    'https://api.battlefy.com/stages/{stage_id}?extend%5Bmatches%5D%5Btop.team%5D%5Bplayers%5D%5Buser%5D=true' \
    '&extend%5Bmatches%5D%5Btop.team%5D%5BpersistentTeam%5D=true' \
    '&extend%5Bmatches%5D%5Bbottom.team%5D%5Bplayers%5D%5Buser%5D=true' \
    '&extend%5Bmatches%5D%5Bbottom.team%5D%5BpersistentTeam%5D=true' \
    '&extend%5Bgroups%5D%5Bteams%5D=true' \
    '&extend%5Bgroups%5D%5Bmatches%5D%5Btop.team%5D%5Bplayers%5D%5Buser%5D=true' \
    '&extend%5Bgroups%5D%5Bmatches%5D%5Btop.team%5D%5BpersistentTeam%5D=true' \
    '&extend%5Bgroups%5D%5Bmatches%5D%5Bbottom.team%5D%5Bplayers%5D%5Buser%5D=true' \
    '&extend%5Bgroups%5D%5Bmatches%5D%5Bbottom.team%5D%5BpersistentTeam%5D=true'
"""Stage info request format. Param is stage_id."""


TOURNAMENT_INFO_FETCH_ADDRESS_FORMAT: str = \
    "https://api.battlefy.com/tournaments/{tourney_id}?" \
    "extend%5Bcampaign%5D%5Bsponsor%5D=true" \
    "&extend%5Bstages%5D%5B%24query%5D%5BdeletedAt%5D%5B%24exists%5D=false" \
    "&extend%5Bstages%5D%5B%24opts%5D%5Bname%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5Bbracket%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BstartTime%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BendTime%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5Bschedule%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BmatchCheckinDuration%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BhasCheckinTimer%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BhasStarted%5D=1" \
    "&extend%5Bstages%5D%5B%24opts%5D%5BhasMatchCheckin%5D=1" \
    "&extend%5Borganization%5D%5Bowner%5D%5B%24opts%5D%5Btimezone%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5Bname%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5Bslug%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5BownerID%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5BlogoUrl%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5BbannerUrl%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5Bfeatures%5D=1" \
    "&extend%5Borganization%5D%5B%24opts%5D%5Bfollowers%5D=1" \
    "&extend%5Bgame%5D=true" \
    "&extend%5Bstreams%5D%5B%24query%5D%5BdeletedAt%5D%5B%24exists%5D=false"
"""Tournament info request format. Param is tourney_id."""

CLOUD_BACKEND: str = 'https://dtmwra1jsgyb0.cloudfront.net'
"""
This is the Cloudfront caching of Battlefy data. This is owned by Battlefy but not part of their public API.
However, it has been made public by
https://www.invenglobal.com/articles/8591/for-months-battlefy-knew-their-faulty-api-was-hurting-hearthstone-esports-integrity-but-the-platform-didnt-bother-telling-anyone
"""

TOURNAMENT_BASIC_INFO_FETCH_ADDRESS_FORMAT: str = CLOUD_BACKEND + '/tournaments/{tourney_id}'
"""Tournament basic info fetch address. Param is the tourney_id."""

TEAMS_FETCH_ADDRESS_FORMAT: str = CLOUD_BACKEND + '/tournaments/{tourney_id}/teams'
"""Tournament teams info fetch address. Param is the tourney_id."""

ORG_ADDRESS_FORMAT: str = CLOUD_BACKEND + '/organizations?' \
                                          'slug={org_slug}' \
                                          '&extend%5Badmins%5D=true' \
                                          '&extend%5Bmoderators%5D=true' \
                                          '&extend%5Bowner%5D=true' \
                                          '&extend%5Brunners%5D=true'
"""Organisation fetch address. Param is the org_slug."""

ORG_SEARCH_FORMAT: str = "https://search.battlefy.com/tournament/organization/{org_id}/past?page={page}&size=10"
"""Organisation search format. 
First param is the org_id to find.
Second param is the page index.
"""
