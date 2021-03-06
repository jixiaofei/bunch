# -*- coding: utf-8 -*-
# <Bunch - BDD test tool for Lettuce scenarios>
# Copyright (c) 2012 Grid Dynamics Consulting Services, Inc, All Rights Reserved
# http://www.griddynamics.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
# DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE
# FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
# DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
# SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
# CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
# OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
# OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

from lettuce import step, world
import pprint
import os

pp = pprint.PrettyPrinter(indent=4)

BUNCH_PATH_ENV_VAR = "CURRENT_BUNCH_DIR"

@step(u'Require setup:? "(.*)"')
def requires_setup(step, Phrase):
    """
        This step checks whether required setups are passed or not.
        It is not launches these setups by itself, instead they are launched
        by the Bunch before launching lettuce.
    """
    pp.pprint(step)

@step(u'Require external setup:? "(.*)"')
def requires_external_setup(step, Phrase):
    """
        This step checks whether required setups are passed or not.
        It is not launches these setups by itself, instead they are launched
        by the Bunch before launching lettuce.
    """
    pp.pprint(step)

def get_current_bunch_dir():
    return os.getenv(BUNCH_PATH_ENV_VAR)

def set_current_bunch_dir(value):
    os.putenv(BUNCH_PATH_ENV_VAR, value)